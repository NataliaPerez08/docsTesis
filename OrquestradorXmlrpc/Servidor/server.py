from xmlrpc.server import SimpleXMLRPCServer
# Mis clases
from usuario import Usuario
import PrivateNetwork as rp
import WG.setup_wg as wg

class Servidor:
    def __init__(self):
        self.servidor = SimpleXMLRPCServer(("0.0.0.0", 8000))
        self.servidor.register_instance(self)
        # Diccionario de redes privadas {id: RedPrivada}
        self.private_networks = dict()
        self.usuario = None
        
        # Contador de redes privadas
        self.private_network_counter = 0

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
        return endpoint.id
    
    def get_endpoints(self, private_network_id):
        private_network = self.get_private_network_by_id(private_network_id)
        return [str(endpoint) for endpoint in private_network.endpoints]

server = Servidor()
print("Listening on port 8000...")
server.iniciar()

