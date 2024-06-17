import ipaddress
from EndPoint import Endpoint

class PrivateNetwork:
    def __init__(self, id_red, name, ip_addr=None, mask_network=None):
        self.id = id_red
        self.name = name
        
        if ip_addr is not None:
           self.ip_addr = ipaddress.IPv4Address(ip_addr)
           self.last_host_assigned = str(ip_addr)
        else:
            self.ip_addr = None
        if mask_network is not None:
            self.mask_network = mask_network
        else:
            self.mask_network = None


        self.available_hosts = list()
        self.last_host_assigned = ""

        self.num_endpoints = 0
        
        # Diccionario de endpoints {id: Endpoint}
        self.endpoints = dict()

    def get_id(self):
        return str(self.id)
    
    def get_name(self):
        return self.name
    
    def get_endpoints(self):
        return self.endpoints
    
    def get_ip_addr(self):
        return self.ip_addr
    
    def get_mask_network(self):
        return self.mask_network
    
    def get_available_hosts(self):
        return self.available_hosts
    
    def get_last_host_assigned(self):
        return self.last_host_assigned
    
    def add_endpoint(self, endpoint):
        print("Agregando endpoint")
        self.endpoints[str(endpoint.id)] = endpoint

    def get_network_mask(self):
        return self.ip_addr.netmask

    def set_ip_addr(self, ip_addr):
        self.ip_addr = ipaddress.IPv4Network(ip_addr)

    def set_network_mask(self, mask_network):
        self.mask_network = mask_network
        ip = self.ip_addr.exploded.split('/')[0]
        self.ip_addr = ipaddress.IPv4Network(f"{ip}/{mask_network}")

    def set_last_host_assigned(self, last_host_assigned):
        self.last_host_assigned = last_host_assigned
    
    def calcule_network_range(self):
        hosts = list(self.ip_addr.hosts())
        self.available_hosts = hosts
        return hosts
    
    def calculate_next_host(self):
        print("Calculando siguiente dirección IP disponible...")
        """Calcula la siguiente dirección IP disponible en la red privada.
            TODO: Validar que la dirección IP no esté en uso, y que no se haya llegado al límite de direcciones IP disponibles.

            return: str
        """
        if self.last_host_assigned == "":
            self.last_host_assigned = self.ip_addr.network_address

        last_host = str(self.last_host_assigned)
        last_host = last_host.split('.')
        last_host[3] = str(int(last_host[3]) + 1)
        self.last_host_assigned = str('.'.join(last_host))
        return self.last_host_assigned
    
    def create_endpoint(self, name) -> Endpoint:
        print("Creando endpoint, nombre: " + name, "ID: " + str(self.num_endpoints))
        
        print(type(self.num_endpoints))
        
        endpoint = Endpoint(id_endpoint=0, name=name, private_network_id=self.id)
        self.num_endpoints += 1
        #self.add_endpoint(endpoint)
        
        return endpoint 

    def __str__(self):
        return "ID: " + str(self.id) + " IP Address: " + str(self.ip_addr) + " Mask Network: " + str(self.mask_network) 