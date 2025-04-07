import gestore_bluetooth as gestore_bluetooth


def main():
    """Funzione principale che avvia il server Bluetooth"""
    try:
        # Avvia il server Bluetooth (delegato al gestore)
        gestore_bluetooth.avvia_server()

    except Exception as e:
        print(f"Errore del server: {e}")
    finally:
        gestore_bluetooth.chiudi_tutto()  # Chiudi tutto per sicurezza
        print("Server fermato")


if __name__ == "__main__":
    main()
