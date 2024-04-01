import socket
from dotenv import load_dotenv

from orquestrador.WG.setup_wg import crear_interfaz_virtual, cargar_configuracion_wireguard

# main
if __name__ == "__main__":
    # Crear socket UDP 
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


    puerto = 1024
    direccion_ip = "localhost"
    mascara_red = "24"

    # Configurar el socket a una dirección IP y puerto específico
    server_address = (direccion_ip, puerto)
    udp_socket.bind(server_address)

    #crear_interfaz_virtual("wg0", direccion_ip, mascara_red)
    #cargar_configuracion_wireguard("wg0", "configuracion_peers.conf")
    

    while True:
        # Receive data from the socket
        data, address = udp_socket.recvfrom(1024)
        # Print the received message
        print(f"Received message: {data.decode()}")

        if data == None:
            break    
    # Close the socket
    udp_socket.close()