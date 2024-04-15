import socket
from _thread import start_new_thread

# Incluir el código de configuración de la interfaz de red
import WG.setup_wg as wg
 
# Función que atiende una conexión. Recibe como parámetro el socket de 
# la conexión y la victima
def threaded(conn, addr):
    try: 
        while True:
            # Recibe un mensaje de la victima
            data = conn.recv(1024)
            if data: 
                try:
                    print("Recibí mensaje del cliente",addr[0],':',addr[1])
                    # Imprime el mensaje recibido
                    print("Cliente:", data.decode())              
                except SyntaxError:
                    print("Recibí mensaje inválido del cliente",addr[0],':',addr[1])
    except socket.timeout:
        print("Timeout. Cerrando conexión con el cliente",addr[0],':',addr[1])
        conn.close()
    except ConnectionAbortedError:
        print("Error de conexión con el cliente",addr[0],':',addr[1])

# Función principal. Crea un socket TCP y escucha conexiones
def Main():
    ip_wg = '10.0.0.2'
    # Configurar la interfaz de red
    wg.crear_interfaz_virtual("wg0", ip_wg, "24")
    wg.iniciar_interfaz_virtual("wg0")
    # Dirección IP y puerto del servidor
    
    host = ip_wg
    port = 80
    # Crear un socket UDP
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    print("El socket está enlazado al puerto", port)
    udp_socket.bind((host, port))
    
	
    while True:
        # Recibe data del socket
        data, address = udp_socket.recvfrom(1024)
        # Print the received message
        print(f"Received message: {data.decode()}")
        print("Conexión establecida con", address[0],':',address[1])
        # Inicia un nuevo hilo para atender la conexión
        #start_new_thread(threaded, (conn,address))
        #sock.close()

if __name__ == '__main__':
	Main()
