import ipaddress
from EndPoint import Endpoint

class RedPrivada:
    def __init__(self, iden, name, ip_addr=None, mask_network=None):
        self.id = iden
        self.name = name
        if ip_addr is not None:
           self.ip_addr = ipaddress.IPv4Address(ip_addr)
        else:
            self.ip_addr = None
        if mask_network is not None:
            self.mask_network = mask_network
        else:
            self.mask_network = None

        self.endpoints = list()

        self.avaliable_hosts = list()
        self.last_host_assigned = ""

        self.num_endpoints = 0

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
    
    def get_avaliable_hosts(self):
        return self.avaliable_hosts
    
    def get_last_host_assigned(self):
        return self.last_host_assigned
    
    def add_endpoint(self, endpoint):
        self.endpoint.append(endpoint)

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
        self.avaliable_hosts = hosts
        return hosts
    
    def add_endpoint(self, name):
        num_endpoints = self.num_endpoints
        endpoint = Endpoint(self, num_endpoints, name, self.id)
        self.num_endpoints += 1
        self.endpoints.append(endpoint)

    def calculate_next_host(self):
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


    def __str__(self):
        return "ID: " + str(self.id) + " IP Address: " + str(self.ip_addr) + " Mask Network: " + str(self.mask_network) 