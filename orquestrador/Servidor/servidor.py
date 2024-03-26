import socket
import subprocess

def crear_interfaz_virtual(nombre_interfaz, direccion_ip, mascara_red):
    try:
        # Crear una interfaz virtual
        subprocess.run(
            ["ip", "link", "add", "dev", nombre_interfaz, "type", "wireguard"]
        )

        # Establecer la dirección IP y la máscara de red para la interfaz virtual
        subprocess.run(
            ["ip", "address", "add", f"{direccion_ip}/{mascara_red}", "dev", nombre_interfaz]
        )

        # Levantar la interfaz virtual
        subprocess.run(["ip", "link", "set", "dev", nombre_interfaz, "up"])

        print(
            f"Interfaz virtual {nombre_interfaz} creada exitosamente con IP {direccion_ip}/{mascara_red}"
        )
    except Exception as e:
        print(f"Error creando interfaz virtual: {e}")

def cargar_configuracion_wireguard(nombre_interfaz, archivo_configuracion):
    try:
        # Cargar la configuración de WireGuard desde el archivo de configuración
        subprocess.run(
            [
                "wg",
                "setconf",
                nombre_interfaz,
                archivo_configuracion,
            ]
        )
    except Exception as e:
        print(f"Error cargando la configuración de WireGuard: {e}")

def iniciar_wireguard(lista_configuracion_peers):
    for peer in lista_configuracion_peers:
        # Ejemplo de configuración de peer:
        delattr


    #wg set wg0 listen-port 51820 private-key /path/to/private-key peer ABCDEF... allowed-ips 192.168.88.0/24 endpoint 209.202.254.14:8172 
    try:
        # Iniciar WireGuard
        subprocess.run(
            [
                "wg",
                "set",
                "wg0",
                "listen-port",
                "51820",
                "private-key",
                "/path/to/private-key",
                "peer",
                "ABCDEF...",
                "allowed-ips",
                "

# main
if __name__ == "__main__":
    # Crear socket UDP 
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


    puerto_origen = 1024
    direccion_ip = "localhost"
    mascara_red = "24"

    # Configurar el socket a una dirección IP y puerto específico
    server_address = (direccion_ip, puerto)
    udp_socket.bind(server_address)

    crear_interfaz_virtual("wg0", direccion_ip, mascara_red)
    cargar_configuracion_wireguard("wg0", "configuracion_peers.conf")
    

    while True:
        # Receive data from the socket
        data, address = udp_socket.recvfrom(1024)
        # Print the received message
        print(f"Received message: {data.decode()}")

        if data == None:
            break    
    # Close the socket
    udp_socket.close()