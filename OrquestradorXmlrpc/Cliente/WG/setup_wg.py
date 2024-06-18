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
