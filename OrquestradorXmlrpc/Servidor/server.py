from xmlrpc.server import SimpleXMLRPCServer
# Mis clases
from usuario import Usuario
import EndPoint as ep
import RedPrivada as rp
import WG.setup_wg as wg

class Servidor:
    def __init__(self):
        self.servidor = SimpleXMLRPCServer(("localhost", 8000))
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

    def create_private_network(self,nombre_red) -> int:
        # Crear la red privada
        red = rp.RedPrivada(self.private_network_counter,nombre_red)
        self.private_network_counter += 1
        # Asignar dirección IP. Asignar máscara de red. Rango de 16 hosts: 14 hosts + 2 direcciones de red y broadcast
        red.set_ip_addr('10.0.0.0')
        red.set_network_mask(28)
        red.set_last_host_assigned('10.0.0.1')
        # Agregar la red a la lista de redes privadas
        self.private_networks[str(red.id)] = str(red)
        return red.id
    
    def get_private_networks(self)->str:
        return self.private_networks

    def get_private_network_by_id(self, net_id):
        return self.private_networks[str(net_id)]        

    def create_endpoint(self, private_network_id, endpoint_name):
        print("Creating endpoint...")
        # Obtener la red privada
        private_network = self.get_private_network_by_id(private_network_id)
        if private_network is None:
            print("Private network not found!")
            return None
        # Crear la dirección IP del endpoint
        endpoint_ip = private_network.calculate_next_host()
        # Crear el endpoint
        endpoint = ep.Endpoint(iden=0, name=endpoint_name, ip_addr=endpoint_ip, private_network_id=private_network_id)
        # Agregar el endpoint a la red privada
        private_network.add_endpoint(endpoint)
        print("Endpoint created successfully!")
        return endpoint.id
    
    def get_endpoints(self, private_network_id):
        print("Getting endpoints...")
        private_network = self.get_private_network_by_id(private_network_id)
        print(private_network)
        if private_network is None:
            print("Private network not found!")
            return None
        str_endpoints = ""
        print(private_network.get_endpoints())
        for endpoint in private_network.get_endpoints():
            print(endpoint)
            str_endpoints += endpoint.__str__() + "\n"
            
        return str_endpoints 

server = Servidor()
print("Listening on port 8000...")
server.iniciar()

