import xmlrpc.client
import sys
import os
from conn_scapy import verificar_conectividad

from WG import ConfiguradorWireguardCliente as wg

# Servidor en la nube
#dir_servidor="http://34.42.253.180:8000/"
# Servidor local
dir_servidor = "http://0.0.0.0:8000/"
dir_servidor = "http://localhost:8000/"
ip_servidor = "0.0.0.0"

class Cliente:
    def __init__(self):
        self.proxy = xmlrpc.client.ServerProxy(dir_servidor)

        # Configurador de Wireguard
        self.wg = wg.ConfiguradorWireguardCliente()

    def register_user(self, name, email, password):
        """
        Registra un usuario en el servidor. Es volatil
        """
        print("Registrando usuario...")
        is_register = self.proxy.register_user(name, email, password)
        if not is_register:
            print("Error al registrar el usuario!")
            return
        print("Usuario registrado!")

    def identify_me(self, email, password):
        """
        Identifica un usuario en el servidor
        """
        print("Identificando usuario...")
        is_identified = self.proxy.identify_user(email, password)
        if not is_identified:
            print("Error al identificar el usuario!")
            return
        print("Usuario identificado!")

    def whoami(self):
        """
        Obtiene el nombre del usuario actual
        """
        return self.proxy.whoami()

    def create_private_network(self, nombre):
        """
        Crea una red privada en el servidor
        """
        print("Creando red privada...")
        private_network_id = self.proxy.create_private_network(nombre)
        if private_network_id == -1:
            print("Error al crear la red privada! Iniciaste sesión?")
            return
        print(f"ID de la red privada: {private_network_id}")

    def get_private_networks(self):
        """
        Recupera las redes privadas del servidor
        """
        priv_net = self.proxy.get_private_networks()
        print("Redes privadas:")
        print(priv_net)

    def crear_endpoint(self, id_red_privada, nombre_endpoint, ip_endpoint, puerto_endpoint):
        print("Creando endpoint...")
        # Crear registro de endpoint en el servidor
        # y registrarlo en el cliente


    def ver_endpoints(self, id_red_privada):
        print("Obteniendo endpoints...")
        print(self.proxy.get_endpoints(id_red_privada))

    def conectar_endpoint(self, id_endpoint, id_red_privada):
        print("Conectando endpoint...")
        # Encontrar la red privada
        private_network = self.proxy.get_private_network_by_id(id_red_privada)

        if private_network == -1:
            print("No se encontro la red")
            return

        # Encontrar dispositivo en la red
        endpoint = private_network.get_endpoint_by_id(id_endpoint)

        if endpoint == -1:
            print("No se encontro el Endpoint")
            return

        print(f"Endpoint: {endpoint}")
        print(f"Red privada: {private_network}")
        verificar_conectividad(endpoint.ip_addr, private_network.last_host_assigned)

    def conectar_endpoint_directo(self, ip_endpoint, puerto_endpoint):
        print("Conectando endpoint directo...")
        verificar_conectividad(ip_endpoint)

    def obtener_clave_publica_servidor(self):
        print("Obteniendo clave pública...")
        print(self.proxy.get_public_key())

    def obtener_configuracion_wireguard_local(self):
        print("Obteniendo configuracion..")
        conf = self.wg.get_wg_state()
        print(conf)

    def obtener_configuracion_wireguard_servidor(self):
        print("Preguntar al servidor")
        print(self.proxy.get_wireguard_config())

    def cerrar_sesion(self):
        print("Cerrando sesión...")
        self.proxy.close_session()
        print("Sesión cerrada!")

    def get_public_ip(self):
        print("Obteniendo IP pública...",self.ip_cliente)
        return ip_cliente

    def add_public_ip(self, ip):
        print("Añadiendo IP pública...",ip, "ip")
        ip_cliente = ip
        print("IP ",self.ip_cliente," añadida!")
        
    # Inicializar Wireguard en el cliente
    def init_wireguard_interface(self, ip_cliente):
        print("Inicializando Wireguard...")
        wg_private_key, wg_public_key = self.wg.create_keys()
        print("Clave privada: ", wg_private_key)
        print("Clave pública: ", wg_public_key)

        self.wg.create_wg_interface(ip_cliente)
        
        # Guardar la clave pública y privada en el cliente
        # Definirlas como de entorno
        os.putenv("WG_PRIVATE_KEY", wg_private_key)
        os.putenv("WG_PUBLIC_KEY", wg_public_key)
        
        print("Wireguard inicializado!") 
    
    
    
    # registrar_como_peer <nombre> <id_red_privada> <ip_cliente> <puerto_cliente> 
    def configure_as_peer(self, nombre_endpoint, id_red_privada, ip_cliente, listen_port):
        print("Configurando como peer...")
        
        endpoint_ip_WG = self.proxy.create_endpoint(id_red_privada, nombre_endpoint)
        if endpoint_ip_WG == -1:
            print("Error al configurar el peer!")
            return
        print("IP de Wireguard asignada: ", endpoint_ip_WG)
       
        # Configurar peer 
        allowed_ips = self.proxy.get_allowed_ips(id_red_privada)
        self.wg.create_peer(wg_public_key, allowed_ips, ip_cliente, listen_port, ip_servidor)

        # Registrar peer en el servidor
        self.proxy.create_peer(wg_public_key, allowed_ips, endpoint_ip_WG, listen_port, ip_cliente)



    def register_peer(self, public_key, allowed_ips, ip_cliente, listen_port, ip_servidor):
        print("Registrando peer...")
        endpoint_ip_WG = self.proxy.create_peer(public_key, allowed_ips, ip_cliente, listen_port, ip_servidor)
        if endpoint_ip_WG == -1:
            print("Error al registrar el peer!")
            return
        print("Peer registrado!")
        print("IP de Wireguard asignada: ", endpoint_ip_WG)
        
        
    def get_client_public_key(self):
        print("Obteniendo clave pública...")
        # Obtener la clave pública del cliente definida con os.putenv
        print(os.getenv("WG_PUBLIC_KEY"))
        return os.getenv("WG_PUBLIC_KEY")

