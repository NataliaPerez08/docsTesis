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
        self.private_networks = list()
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
        print("Creating private network...")
        # Crear la red privada
        red = rp.RedPrivada(self.private_network_counter,nombre_red)
        self.private_network_counter += 1

        # Asignar dirección IP
        # Asignar máscara de red. Rango de 16 hosts: 14 hosts + 2 direcciones de red y broadcast
        red.set_ip_addr('10.0.0.0')
        red.set_network_mask(28)
        red.set_last_host_assigned('10.0.0.1')

        print(f"IP address: {red.get_ip_addr()}")
        print(f"Network mask: {red.get_network_mask()}")
        print(f"Network address: {red.calcule_network_range()}")
        print(f"Broadcast address: {red.calcule_network_range()[-1]}")
        print("Private network created successfully!")

        # Agregar la red a la lista de redes privadas
        self.private_networks.append(red)

        # Interfaz de red privada
        print("Creating private network interface...")
        wg.create_interface(interface_name=nombre_red, ip_addr='10.0.0.0', mask_network=28)
        # Retornar el identificador de la red
        return red.id
    
    def get_private_networks(self)->str:
        print("Getting private networks...")
        str_private_networks = ""
        for private_network in self.private_networks:
            str_private_networks += private_network.__str__() + "\n"
        return str_private_networks

    def get_private_network_by_id(self, net_id):
        for private_network in self.private_networks:
            if int(private_network.id) == int(net_id):
                return private_network
        return None

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

