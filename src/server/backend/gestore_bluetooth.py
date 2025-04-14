import threading
import time
import bluetooth
import json

from config import (
    NOME_DISPOSITIVO_BLUETOOTH,
    UUID_BLUETOOTH,
    DIMENSIONE_BUFFER,
    CONNESSIONI_MASSIME,
    TIMEOUT,
)

# Variabili globali
connessioni = []
blocco_connessione = threading.Lock()
in_esecuzione = True
socket_server = None


def avvia_server():
    """Avvia il server Bluetooth e gestisce le connessioni"""
    global in_esecuzione, socket_server

    # Inizializza il socket del server
    socket_server = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    socket_server.bind(("", 3))
    socket_server.listen(CONNESSIONI_MASSIME)
    porta = socket_server.getsockname()[1]

    # Pubblicizza il servizio
    bluetooth.advertise_service(
        socket_server,
        NOME_DISPOSITIVO_BLUETOOTH,
        service_id=UUID_BLUETOOTH,
        service_classes=[UUID_BLUETOOTH, bluetooth.SERIAL_PORT_CLASS],
        profiles=[bluetooth.SERIAL_PORT_PROFILE],
    )

    print(f"Server Bluetooth '{NOME_DISPOSITIVO_BLUETOOTH}' avviato su RFCOMM {porta}")
    print("Premi Ctrl+C per fermare il server")

    in_esecuzione = True

    try:
        while in_esecuzione:
            # Accetta e gestisci connessioni
            socket_client, info_client = socket_server.accept()
            thread = threading.Thread(target=gestisci_client, args=(socket_client, info_client))
            thread.daemon = True
            thread.start()
    except KeyboardInterrupt:
        print("\nServer interrotto dall'utente")
    finally:
        chiudi_tutto()


def gestisci_client(socket_client, info_client):
    """Gestisce la comunicazione con un client"""
    with blocco_connessione:
        connessioni.append(socket_client)

    print(f"Client {info_client} connesso. Clienti totali: {len(connessioni)}")

    socket_client.settimeout(TIMEOUT)
    try:
        while in_esecuzione:
            try:
                dati = socket_client.recv(DIMENSIONE_BUFFER)
                if dati:
                    elabora_dati(dati.decode("utf-8"), info_client)
            except bluetooth.btcommon.BluetoothError as e:
                if "timed out" in str(e):
                    print(f"Timeout client {info_client}")
                    break
                else:

                    print(f"Errore Bluetooth: {e}")
                    break
    finally:
        with blocco_connessione:
            if socket_client in connessioni:
                connessioni.remove(socket_client)
        socket_client.close()
        print(f"Client {info_client} disconnesso. Clienti rimanenti: {len(connessioni)}")


def elabora_dati(dati, info_client):
    """Elabora i dati ricevuti dal client e li salva in formato JSON"""
    # Parse JSON data
    dati_json = json.loads(dati)
    
    # Extract hostname from data or use client info address as fallback
    hostname = dati_json.get("hostname", str(info_client[0]))
    
    # Carica il database
    with open("database.json", "r") as file:
        database = json.load(file)
    
    # Aggiorna o aggiungi i dati del dispositivo
    database["dispositivi"][hostname] = dati_json.get("data", {})
    

    
    # Salva il database aggiornato
    with open("database.json", "w") as file:
        json.dump(database, file, indent=2)
        
    print(f"Dati salvati per il dispositivo: {hostname} ({info_client[0]})")


def chiudi_tutto():
    """Chiude tutte le connessioni client e il server"""
    global socket_server, in_esecuzione

    in_esecuzione = False
    print("Chiusura connessioni...")

    with blocco_connessione:
        for conn in connessioni[:]:
            try:
                conn.close()
            except Exception:
                pass
        connessioni.clear()

    if socket_server:
        socket_server.close()
