import subprocess
import os

def create_interface(interface_name, ip_addr, mask_network):
    try:
        # Verificar si es windows o linux
        if os.name == "nt":
            ip_addr = ip_addr.__str__()
            subprocess.run(["netsh", "interface", "ipv4", "set", "address", "name=", interface_name, "source=static", f"address={ip_addr}", f"mask={mask_network}"])
            print(f"Netsh interface ipv4 set address name={interface_name} source=static address={ip_addr} mask={mask_network}")
            return
        else:
            print("Linux")
            # Crear una interfaz virtual
            subprocess.run(
                ["ip", "link", "add", "dev", interface_name, "type", "wireguard"]
            )
            print("IP link add dev wg0 type wireguard")

            # Establecer la dirección IP y la máscara de red para la interfaz virtual
            subprocess.run(
                ["ip", "address", "add", f"{ip_addr}/{mask_network}", "dev", interface_name]
            )
            print(f"IP address add {ip_addr}/{mask_network} dev {interface_name}")

            # Levantar la interfaz virtual
            subprocess.run(["ip", "link", "set", "dev", interface_name, "up"])

            print(
                f"Interfaz virtual {interface_name} creada exitosamente con IP {ip_addr}/{mask_network}"
            )
    except Exception as e:
        print(f"Error creando interfaz virtual: {e}")

def start_virtual_interface(interface_name):
    try:
        # Crea la llave privada para la interfaz virtual
        subprocess.run(["wg", "genkey", ">", "/etc/wireguard/privatekey"])
        # Crea la llave publica para la interfaz virtual
        subprocess.run(["wg", "pubkey", "<", "/etc/wireguard/privatekey", ">", "/etc/wireguard/publickey"])
        # Establecer la llave privada para la interfaz virtual
        subprocess.run(["wg", "set", interface_name, "private-key /etc/wireguard/privatekey"])
        # Establecer la llave publica para la interfaz virtual
        subprocess.run(["wg", "set", interface_name, "public-key /etc/wireguard/publickey"])

        # Iniciar la interfaz virtual
        subprocess.run(["wg", "set", interface_name, "up"])

        # Iniciar la interfaz virtual con ip
        subprocess.run(["ip", "link", "set", "dev", interface_name, "up"])
    except Exception as e:
        print(f"Error iniciando interfaz virtual: {e}")

def load_wg_config(interface_name, conf_file):
    try:
        # Cargar la configuración de WireGuard desde el archivo de configuración
        subprocess.run(
            [
                "wg",
                "setconf",
                interface_name,
                conf_file,
            ]
        )
    except Exception as e:
        print(f"Error cargando la configuración de WireGuard: {e}")


def start_wireguard(listen_port, lista_peers,private_key):
    # Crear la configuración de los peers
    conf_peers = ""
    for peer in lista_peers:
        conf_peers += f"peer {peer}\n"
        conf_peers += f"allowed-ips: {peer['allowed_ips']}\n"
        conf_peers += f"endpoint {peer['endpoint']}\n"
    
    #wg set wg0 listen-port 51820 private-key /path/to/private-key peer ABCDEF... allowed-ips 192.168.88.0/24 endpoint 209.202.254.14:8172 
    try:
        # Iniciar WireGuard
        subprocess.run(
            [
                "wg",
                "set",
                "wg0",
                "listen-port",
                listen_port,
                private_key,
                "/etc/wireguard/privatekey",
                conf_peers
            ])
    except Exception as e:
        print(f"Error iniciando WireGuard: {e}")

def select_ip():
    # Clase A: 10.0.0.0 a 10.255.255.255
    ip_a = "10. 0. 0. 0"
    # Clase B: 172.16.0.0 a 172.31.255.255
    ip_b = "172.16. 0. 0"
    # Clase C:
    ip_c = "192.168. 0. 0"

    return ip_a