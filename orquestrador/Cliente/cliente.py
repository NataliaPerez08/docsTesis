import json
import socket

import WG.setup_wg

# Create a TCP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Send data to server
server_address = ('localhost', 80)

# Access the server
sock.connect(server_address)

# Crear interfaz de red wg0
ip_wireguard = '10.0.0.1'
WG.setup_wg.crear_interfaz_virtual('wg0', ip_wireguard, 24)

while True:
    print("Iniciar sesion")
    usuario = input("Ingrese usuario/ID: ")

    input_data = {'usr': usuario,'ip_interfaz_wireguard': ip_wireguard}
    # JSON
    input_data = json.dumps(input_data)
    if input_data == "exit":
        break

    sock.sendto(input_data.encode(), server_address)

# Close the socket
sock.close()