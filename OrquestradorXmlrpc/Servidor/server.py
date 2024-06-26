from xmlrpc.server import SimpleXMLRPCServer
# Mis clases
from usuario import Usuario
import PrivateNetwork as rp
import WG.configGenerator as wg

class Servidor:
    def __init__(self):
        self.servidor = SimpleXMLRPCServer(("0.0.0.0", 8000))
        self.servidor.register_instance(self)
        # Diccionario de redes privadas {id: RedPrivada}
        self.private_networks = dict()
        self.usuario = None
        
        # Contador de redes privadas
        self.private_network_counter = 0
        
        # Llave pública de Wireguard del orquestrador
        self.wg_private_key = None
        self.wg_public_key = None

    def iniciar(self):
        self.servidor.serve_forever()
    
    def set_user(self, name, email, password):
        print("Setting user...")
        self.usuario = Usuario(name, email, password)
        print("User set successfully!")

    def create_private_network(self,net_name) -> int:
        # Crear la red privada
        red = rp.PrivateNetwork(self.private_network_counter, net_name,'10.0.0.0', 28)
        self.private_network_counter += 1
        # Agregar la red a la lista de redes privadas
        self.private_networks[str(red.id)] = red
        return red.id
    
    def get_private_networks(self)->str:
        return [str(red) for red in self.private_networks.values()]
    

    def get_private_network_by_id(self, net_id):
        return self.private_networks[str(net_id)]    

    def create_endpoint(self, private_network_id, endpoint_name):
        private_network = self.get_private_network_by_id(private_network_id)
        endpoint = private_network.create_endpoint(endpoint_name)
        return endpoint.get_wireguard_ip()
    
    def get_endpoints(self, private_network_id):
        private_network = self.get_private_network_by_id(private_network_id)
        return private_network.endpoints
    
    def get_public_key(self):
        return self.wg_public_key
    
    def get_allowed_ips(self, private_network_id):
        private_network = self.get_private_network_by_id(private_network_id)
        return private_network.get_available_hosts()
    
    def create_peer(self,public_key, allowed_ips, endpoint_ip_WG, listen_port):
        print("Creating peer...")
        pass
    
    def init_wireguard(self):
        # Crear las claves pública y privada
        private_key, public_key = wg.create_keys()
        self.wg_public_key = public_key
        self.wg_private_key = private_key
        

server = Servidor()
server.init_wireguard()
print("Listening on port 8000...")
server.iniciar()

