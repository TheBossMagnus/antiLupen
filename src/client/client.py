import socket
import time
from get_data import organizza_dati

server_addr = "2C:CF:67:99:D4:0E"
port = 3

socket = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)

try:
    print(f"Connessione al server {server_addr}...")
    socket.connect((server_addr, port))
    print("connessione avvenuta con successo")

    while True:
        time.sleep(5)
        data = organizza_dati()  # Call the function to get the data
        socket.send(data.encode())  # Encode the returned string

except Exception as e:
    print(f"Errore: {e}")

finally:
    print("Chiusura connesione")
    socket.close()
