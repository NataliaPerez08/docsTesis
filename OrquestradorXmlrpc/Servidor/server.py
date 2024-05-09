from xmlrpc.server import SimpleXMLRPCServer
# Mis clases
import RedPrivada as rp
import WG.setup_wg as wg

class Servidor:
    def __init__(self):
        self.servidor = SimpleXMLRPCServer(("localhost", 8000))
        self.servidor.register_instance(self)
        self.private_networks = list()

    def iniciar(self):
        self.servidor.serve_forever()

    def is_even(self, n):
        return n % 2 == 0

    def create_private_network(self,nombre_red) -> int:
        print("Creating private network...")
        # Crear la red privada
        red = rp.RedPrivada(0,nombre_red)

        # Asignar dirección IP
        # Asignar máscara de red. Rango de 16 hosts: 14 hosts + 2 direcciones de red y broadcast
        red.set_ip_addr('10.0.0.0')
        red.set_network_mask(28)

        print(f"IP address: {red.get_ip_addr()}")
        print(f"Network mask: {red.get_network_mask()}")
        print(f"Network address: {red.calcule_network_range()}")
        print(f"Broadcast address: {red.calcule_network_range()[-1]}")
        print("Private network created successfully!")

        # Agregar la red a la lista de redes privadas
        self.private_networks.append(red)

        # Interfaz de red privada
        print("Creating private network interface...")
        wg.create_interface(red.id, red.ip_addr, red.mask_network)
        # Retornar el identificador de la red
        return red.id
    
    def get_private_networks(self)->str:
        print("Getting private networks...")
        str_private_networks = ""
        for private_network in self.private_networks:
            str_private_networks += private_network.__str__() + "\n"
        return str_private_networks


server = Servidor()
print("Listening on port 8000...")
server.iniciar()

