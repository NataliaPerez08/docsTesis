import subprocess
import os

class ConfiguradorWireguardCliente:
    def __init__(self):
        private_key, public_key = self.create_keys()
        self.private_key = private_key
        self.public_key = public_key
        
        self.listen_port = 51820

    def create_keys(self):
        """
        Genera las claves pública y privada de Wireguard.
        """
        #print("Generando claves...")
        # Generar clave privada
        private_key = subprocess.run(["wg", "genkey"], stdout=subprocess.PIPE)

        # Llave privada en bytes
        private_key = private_key.stdout

        # Generar clave pública
        public_key = subprocess.run(["wg", "pubkey"], input=private_key, stdout=subprocess.PIPE)

        public_key = public_key.stdout.decode("utf-8").strip()

        # De bytes a string
        private_key = private_key.decode("utf-8").strip()

        return private_key, public_key

    def create_wg_interface(self, ip_wg):
        """
        Crea una interfaz de Wireguard.
        """
        print("Creando interfaz...")
        # Si es Linux
        if os.name == "posix":
            # Verificar si existe la interfaz
            if os.system("ip link show wg0") == 0:
                print("La interfaz ya existe.")
            else:
                print("La interfaz no existe.")
                os.system(f"ip link add dev wg0 type wireguard")
                os.system(f"ip address add {ip_wg} dev wg0")

            # Configurar la interfaz
            print(f"Comando: wg set wg0 listen-port {self.listen_port} private-key <(echo {self.private_key})")
            os.system(f"wg set wg0 listen-port {self.listen_port} private-key <(echo {self.private_key})")

            os.system("ip link set up dev wg0")
        else:
            print("Sistema operativo no soportado.")

    def create_peer(self, public_key, allowed_ips, endpoint_ip, listen_port, ip_servidor):
        
    # Actualizar la configuración de la interfaz. Añadir peer.
    # Man de Wireguard
    #        addconf <interface> <configuration-filename>
    #               Appends the contents of <configuration-filename>, which
    #               must be in the format described by CONFIGURATION FILE
    #               FORMAT below, to the current configuration of <interface>.
    #     syncconf <interface> <configuration-filename>
    #               Like setconf, but reads back the existing configuration
    #               first and only makes changes that are explicitly different
    #               between the configuration file and the interface. This is
    #               much less efficient than setconf, but has the benefit of
    #               not disrupting current peer sessions. The contents of
    #               <configuration-filename> must be in the format described
    #               by CONFIGURATION FILE FORMAT below.
        # Añadir peer
        print("Añadiendo peer...")
        
        #wg set wg0 listen-port 51820 private-key /path/to/private-key peer ABCDEF... allowed-ips 192.168.88.0/24 endpoint 209.202.254.14:8172
        allowed_ips = "10.0.0.0/24"
        # sudo wg set wg10  peer pAY9t1yQPi4lVD84YULYhdiWGhECf2SRs7pll2Vnrgw= allowed-ips 192.168.2.0/24 endpoint 34.42.253.180:51820
        print(f"wg set wg0 peer {public_key} allowed-ips {allowed_ips} endpoint {endpoint_ip}:{listen_port}")
        os.system(f"wg set wg0 peer {public_key} allowed-ips {allowed_ips} endpoint {endpoint_ip}:{listen_port}")

    def get_wg_state(self):
        """
        Obtiene el estado de Wireguard.
        """
        print("Obteniendo estado de Wireguard...")
        # Guardar resultado en una variable
        result = subprocess.run(["wg"], stdout=subprocess.PIPE).stdout.decode("utf-8")
        return result
        
    def get_wg_interface(self):
        """
        Obtiene la interfaz de Wireguard.
        """
        print("Obteniendo interfaz de Wireguard...")
        os.system("ip a show wg0")

    def get_wg_interface_config(self):
        """
        Obtiene la configuración de la interfaz de Wireguard.
        """
        print("Obteniendo configuración de la interfaz de Wireguard...")
        os.system("wg showconf wg0")
