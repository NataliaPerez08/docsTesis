import json
import socket
from _thread import start_new_thread

# Incluir el modulo de configuración de la interfaz de red
import WG.setup_wg 
# Incluir el modulo de recuperación de registros
import usuario 
# Incluir el modulo de configuración de la interfaz de red
import WG.networking_info
 
# Función que atiende una conexión. Recibe como parámetro el socket de 
# la conexión y la dirección del cliente
def threaded(conn, addr):
    try: 
        while True:
            # Recibe un mensaje del cliente
            data = conn.recv(1024)
            if data: 
                try:
                    print("Recibí mensaje del cliente",addr[0],':',addr[1])
                    # Imprime el mensaje recibido
                    print("Cliente:", data.decode()) 
                    # Decodifica el mensaje como json
                    msg_decoded = data.decode()
                    msg_decoded = json.loads(msg_decoded)
                    print(msg_decoded['usr'])
                    print(msg_decoded['ip_interfaz_wireguard'])

                    cliente = msg_decoded['usr']
                    ip_wg_cliente = msg_decoded['ip_interfaz_wireguard']
                    

                    # Crea la interfaz de red wg0
                    ip_wireguard = msg_decoded['ip_interfaz_wireguard']
                    WG.setup_wg.crear_interfaz_virtual('wg0', ip_wireguard, 24)

                    usr = usuario.Usuario(cliente, "1234")
    

                    # Recupera los endpoints del cliente
                    endpoints = usr.recuperar_endpoints()
                    print("Endpoints:", endpoints)

                    # Envia los endpoints al cliente
                    conn.sendall(json.dumps(endpoints).encode())

                    # Muestra la configuración de la interfaz de red iptables
                    print(WG.networking_info.recupera_iptables())




                    print          
                except SyntaxError:
                    print("Recibí mensaje inválido del cliente",addr[0],':',addr[1])
    except socket.timeout:
        print("Timeout. Cerrando conexión con el cliente",addr[0],':',addr[1])
        conn.close()
    except ConnectionAbortedError:
        print("Error de conexión con el cliente",addr[0],':',addr[1])

# Función principal. Crea un socket TCP y escucha conexiones
def Main():
    # Dirección IP y puerto del servidor
    host = 'localhost'
    port = 80
    # Crear un socket TCP
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    print("El socket está enlazado al puerto", port)
    tcp_socket.bind((host, port))
    
    tcp_socket.listen(5)
	
    while True:
        # Recibe data del socket
        conn, address = tcp_socket.accept()
        
        print("Conexión establecida con", address[0],':',address[1])
        # Inicia un nuevo hilo para atender la conexión
        start_new_thread(threaded, (conn,address))
        #sock.close()

if __name__ == '__main__':
	Main()
