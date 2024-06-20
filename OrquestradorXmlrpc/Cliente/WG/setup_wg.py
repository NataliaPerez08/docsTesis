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
    
def create_interface_config_wg(private_key, addr):
    print(f"Comando: wg set wg0 private-key {private_key} listen-port 51820")
    os.system(f"wg set wg0 private-key {private_key} listen-port 51820")

def create_peer(public_key, allowed_ips, endpoint_ip, listen_port):
    """Crea un nuevo peer en el archivo de configuración de Wireguard.
    """
    print("Creando peer...")

    # Cargar configuración de Wireguard
    print(f"Comando: wg set wg0 peer {public_key} allowed-ips {allowed_ips} endpoint {endpoint_ip}:{listen_port}")
    
    os.system(f"wg set wg0 peer {public_key} allowed-ips {allowed_ips} endpoint {endpoint_ip}:{listen_port}")
    