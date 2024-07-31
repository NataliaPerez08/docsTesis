from xmlrpc.server import SimpleXMLRPCServer
import os

# Mis clases
from usuario import Usuario
import PrivateNetwork as rp
import WG.configGeneratorServer as wg

class Servidor:
    def __init__(self):
        dir = "0.0.0.0"
        dir = "localhost"
        self.xmlrpc_server = SimpleXMLRPCServer((dir, 8000))
        self.xmlrpc_server.register_instance(self)

        # Usuario actual
        self.usuario = None

        # Lista de usuarios [id: Usuario]
        self.usuarios = dict()

        # Llave pública de Wireguard del orquestrador
        self.wg_private_key = None
        self.wg_public_key = None

    def iniciar(self):
        """
        Inicia el servidor
        """
        self.xmlrpc_server.serve_forever()

    def register_user(self, name, email, password):
        """
        Registra un usuario en el servidor
        """
        print("Registrando usuario...")
        if email in self.usuarios:
            return False
    
        self.usuario = Usuario(name, email, password)
        self.usuarios[email] = self.usuario
        print("Usuario registrado",self.usuario.name,"!")
        print(self.usuarios)
        return True

    def identify_user(self, email, password):
        """
        Identifica a un usuario en el servidor
        """
        print("Buscando usuario...")
        
        try:
            usuario = self.usuarios[email]
            if usuario is not None and usuario.password == password:
                self.usuario = usuario
                print("Usuario identificado!")
                return True
        except:
            return False
        return  False 
    
    def whoami(self):
        """
        Recupera el usuario actual
        """
        if self.usuario is None:
            return "No hay usuario"
        else:
            return self.usuario.name

    def close_session(self):
        """
        Cierra la sesión del usuario
        """
        self.usuario = None
        return True

    def create_private_network(self,net_name) -> int:
        """
        Crea una red privada
        """
        if self.usuario is None:
            return -1
        else:
            # Crear la red privada
            counter = self.usuario.private_network_counter
            red = rp.PrivateNetwork(counter, net_name,'10.0.0.0', 28)
            self.usuario.private_networks[str(red.id)] = red
            self.usuario.private_network_counter += 1
            return red.id
        
    def whoami(self):
        """
        Recupera el usuario actual
        """
        if self.usuario is None:
            return "No hay usuario"
        else:
            return self.usuario.name

    def get_private_networks(self)->list[str]:
        """
        Recupera las redes privadas del usuario
        """
        if self.usuario is None:
            return ["No hay usuario"]
        else:
            user_private_networks = self.usuario.get_private_networks()
            return [str(red) for red in user_private_networks.values()]

    def get_private_network_by_id(self, net_id):
        """
        Recupera una red privada por su id
        """
        if self.usuario is None:
            return
        else:
            return self.usuario.get_private_network_by_id(net_id)

    def create_endpoint(self, private_network_id, endpoint_name):
        """
        Crea un endpoint en una red privada
        """
        if self.usuario is None:
            return -1
        else:
            private_network = self.get_private_network_by_id(private_network_id)
            if private_network is None:
                return -1
            endpoint = private_network.create_endpoint(endpoint_name)
            return endpoint.get_wireguard_ip()

    def get_endpoints(self, private_network_id):
        """
        Recupera los endpoints de una red privada
        """
        if self.usuario is None:
            return
        else:
            private_network = self.get_private_network_by_id(private_network_id)
            return private_network.endpoints

    def get_public_key(self):
        """
        Recupera la llave pública de Wireguard del orquestrador
        """
        return self.wg_public_key

    def get_allowed_ips(self, private_network_id):
        """
        Recupera las IPs permitidas de una red privada
        """
        private_network = self.get_private_network_by_id(private_network_id)
        if private_network is None:
            return -1
        return private_network.get_allowed_ips()
        

    def get_wireguard_config(self):
        result = wg.get_wg_state()
        print(type(result))
        return wg.get_wg_state()

    def init_wireguard(self):
        # Crear las claves pública y privada
        private_key, public_key = wg.create_keys()
        self.wg_public_key = public_key
        self.wg_private_key = private_key

        ip_wg = "10.0.0.1"
        wg.create_wg_interface(ip_wg=ip_wg, public_key=public_key, private_key=private_key)


server = Servidor()
server.init_wireguard()
print("Listening on port 8000...")
server.iniciar()

