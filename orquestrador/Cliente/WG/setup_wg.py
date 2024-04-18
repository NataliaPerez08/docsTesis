import subprocess
# importar dotenv
from dotenv import load_dotenv
import os

# Cargar las variables de entorno
load_dotenv()

def crear_interfaz_virtual(nombre_interfaz, direccion_ip, mascara_red):
    try:
        # Crear una interfaz virtual
        subprocess.run(
            ["ip", "link", "add", "dev", nombre_interfaz, "type", "wireguard"]
        )

        # Establecer la dirección IP y la máscara de red para la interfaz virtual
        subprocess.run(
            ["ip", "address", "add", f"{direccion_ip}/{mascara_red}", "dev", nombre_interfaz]
        )

        # Levantar la interfaz virtual
        subprocess.run(["ip", "link", "set", "dev", nombre_interfaz, "up"])

        print(
            f"Interfaz virtual {nombre_interfaz} creada exitosamente con IP {direccion_ip}/{mascara_red}"
        )
    except Exception as e:
        print(f"Error creando interfaz virtual: {e}")

def iniciar_interfaz_virtual(nombre_interfaz):
    try:
        # Crea la llave privada para la interfaz virtual
        subprocess.run(["wg", "genkey", ">", "/etc/wireguard/privatekey"])
        # Crea la llave publica para la interfaz virtual
        subprocess.run(["wg", "pubkey", "<", "/etc/wireguard/privatekey", ">", "/etc/wireguard/publickey"])
        # Establecer la llave privada para la interfaz virtual
        subprocess.run(["wg", "set", nombre_interfaz, "private-key /etc/wireguard/privatekey"])
        # Establecer la llave publica para la interfaz virtual
        subprocess.run(["wg", "set", nombre_interfaz, "public-key /etc/wireguard/publickey"])

        # Iniciar la interfaz virtual
        subprocess.run(["wg", "set", nombre_interfaz, "up"])

        # Iniciar la interfaz virtual con ip
        subprocess.run(["ip", "link", "set", "dev", nombre_interfaz, "up"])
    except Exception as e:
        print(f"Error iniciando interfaz virtual: {e}")

def cargar_configuracion_wireguard(nombre_interfaz, archivo_configuracion):
    try:
        # Cargar la configuración de WireGuard desde el archivo de configuración
        subprocess.run(
            [
                "wg",
                "setconf",
                nombre_interfaz,
                archivo_configuracion,
            ]
        )
    except Exception as e:
        print(f"Error cargando la configuración de WireGuard: {e}")


def iniciar_wireguard(listen_port, lista_peers,private_key):
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
                "/path/to/private-key",
                conf_peers
            ])
    except Exception as e:
        print(f"Error iniciando WireGuard: {e}")

def crear_peer(endpoint, allowed_ips, public_key, private_key=""):
    # Definir la configuración del nuevo peer
    if private_key == "":
        peer = {
            "endpoint": endpoint,
            "allowed_ips": allowed_ips,
            "public_key": public_key,
        }
    else:
        peer = {
            "endpoint": endpoint,
            "allowed_ips": allowed_ips,
            "public_key": public_key,
            "private_key": private_key,
        }
    return peer