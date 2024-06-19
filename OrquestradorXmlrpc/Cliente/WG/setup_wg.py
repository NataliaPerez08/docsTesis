import subprocess
import os

def create_keys():
    """Genera las claves pública y privada de Wireguard.
    """
    print("Generando claves...")
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

def create_peer(public_key, allowIPs, endpoint, port):
    """Crea un peer en la configuración de Wireguard.
    """
    print("Creando peer...")
    
def obtener_ip():
    """Obtiene la dirección IP de la máquina.
    """
    print("Obteniendo dirección IP...")
    ip = subprocess.run(["hostname", "-I"], stdout=subprocess.PIPE)
    ip = ip.stdout.decode("utf-8").strip()
    
    return ip

print(obtener_ip())