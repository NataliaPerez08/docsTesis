import xmlrpc.client
import sys
from conn_scapy import verificar_conectividad

import WG.configGeneratorCliente as wg

# Servidor en la nube
#dir_servidor="http://34.42.253.180:8000/"
# Servidor local
dir_servidor = "http://0.0.0.0:8000/"
dir_servidor = "http://localhost:8000/"

class Cliente:
    def __init__(self):
        self.proxy = xmlrpc.client.ServerProxy(dir_servidor)
        self.wg_private_key = None
        self.wg_public_key = None

    def register_user(self, name, email, password):
        print("Registrando usuario...")
        self.proxy.set_user(name, email, password)
        print("Usuario registrado!")
    
    def create_private_network(self, nombre):
        print("Creando red privada...")
        private_network_id = self.proxy.create_private_network(nombre)
        print(f"ID de la red privada: {private_network_id}")
    
    def get_private_networks(self):
            priv_net = self.proxy.get_private_networks()
            print("Redes privadas:")
            for net in priv_net:
                print(net)
            return self.proxy.get_private_networks()
    
    def crear_endpoint(self, id_red_privada, nombre_endpoint):
        print("Creando endpoint...")
        
        endpoint_ip_WG = self.proxy.create_endpoint(id_red_privada, nombre_endpoint)
        # Registrar el host actual como endpoint en la red privada con el servidor.
        # Generar configuración de Wireguard.
        private_key, public_key = wg.create_keys()
        self.wg_private_key = private_key
        self.wg_public_key = public_key
        
        listen_port = 51820
        # Recuperar las allowed IPs de la red privada.
        allowed_ips = self.proxy.get_allowed_ips(id_red_privada)
  
        # Crear interfaz de Wireguard (En el cliente)
        # Si el sistema no es Windows
        if sys.platform != 'win32':           
            wg.create_wg_interface(ip_wg=endpoint_ip_WG, private_key=private_key, peer_public_key=public_key, peer_allowed_ips=allowed_ips, peer_endpoint_ip=dir_servidor, peer_listen_port=listen_port)
        print("IP de Wireguard asignada: ", endpoint_ip_WG)
        
        # Crear peer en el servidor
        #self.proxy.create_peer(public_key, allowed_ips, endpoint_ip_WG, listen_port)
        
    def ver_endpoints(self, id_red_privada):
        print("Obteniendo endpoints...")
        print(self.proxy.get_endpoints(id_red_privada))
        
    def conectar_endpoint(self, id_endpoint, id_red_privada):
        print("Conectando endpoint...")
        endpoint = self.proxy.get_endpoint_by_id(id_endpoint)
        private_network = self.proxy.get_private_network_by_id(id_red_privada)
        if endpoint is None or private_network is None:
            print("Endpoint o red privada no encontrados!")
        print(f"Endpoint: {endpoint}")
        print(f"Red privada: {private_network}")
        verificar_conectividad(endpoint.ip_addr, private_network.last_host_assigned)
        
    def conectar_endpoint_directo(self, ip_endpoint, puerto_endpoint):
        print("Conectando endpoint directo...")
        verificar_conectividad(ip_endpoint)
        
    def obtener_clave_publica_servidor(self):
        print("Obteniendo clave pública...")
        print(self.proxy.get_public_key())
        
        
        
# Manejo por linea de comandos
# python3 client.py registrar_usuario <nombre> <email> <password>
# python3 client.py identificar_usuario <email> <password>
# python3 client.py obtener_clave_publica_servidor
# python3 client.py cerrar_sesion


# python3 client.py crear_red_privada <nombre>
# python3 client.py ver_redes_privadas 
# python3 client.py crear_endpoint <id_red_privada> <nombre_endpoint>
# python3 client.py ver_endpoints <id_red_privada>
# python3 client.py conectar_endpoint <id_endpoint> <id_red_privada>
# python3 client.py conectar_endpoint_directo <ip_wg_endpoint> <puerto_wg_endpoint>
if __name__ == "__main__":
    client = Cliente()
    if len(sys.argv) < 2:
        print("Uso: python3 client.py <comando> <argumentos>")
        sys.exit()
    comando = sys.argv[1]
    
    if comando == "registrar_usuario":
        if len(sys.argv) != 5:
            print("Uso: python3 client.py registrar_usuario <nombre> <email> <password>")
            sys.exit()
        client.register_user(sys.argv[2], sys.argv[3], sys.argv[4])                     
        
    elif comando == "crear_red_privada":
        if len(sys.argv) != 3:
            print("Uso: python3 client.py crear_red_privada <nombre>")
            sys.exit()
        client.create_private_network(sys.argv[2])
        
    elif comando == "ver_redes_privadas":
        client.get_private_networks()
        
    elif comando == "crear_endpoint":
        if len(sys.argv) != 4:
            print("Uso: python3 client.py crear_endpoint <id_red_privada> <nombre_endpoint>")
            sys.exit()
        client.crear_endpoint(sys.argv[2], sys.argv[3])
        
    elif comando == "ver_endpoints":
        if len(sys.argv) != 3:
            print("Uso: python3 client.py ver_endpoints <id_red_privada>")
            sys.exit()
        client.ver_endpoints(sys.argv[2])
        
    elif comando == "conectar_endpoint":
        if len(sys.argv) != 4:
            print("Uso: python3 client.py conectar_endpoint <id_endpoint> <id_red_privada>")
            sys.exit()
        client.conectar_endpoint(sys.argv[2], sys.argv[3])
        
    elif comando == "conectar_endpoint_directo":
        if len(sys.argv) != 4:
            print("Uso: python3 client.py conectar_endpoint_directo <ip_wg_endpoint> <puerto_wg_endpoint>")
            sys.exit()
        client.conectar_endpoint_directo(sys.argv[2], sys.argv[3])
        
    elif comando == "obtener_clave_publica_servidor":
        client.obtener_clave_publica_servidor()