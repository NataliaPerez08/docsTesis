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

def create_peer(public_key, allowed_ips, endpoint_ip, listen_port):
    """Crea un nuevo peer en el archivo de configuración de Wireguard.
    """
    print("Creando peer...")

    # Añadir peer a la configuración actual de Wireguard
    # Wireguard such as addconf or syncconf
    

def create_wg_interface(ip_wg, private_key, peer_public_key, peer_allowed_ips, peer_endpoint_ip, peer_listen_port):
    """Crea una interfaz de Wireguard.
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
        print(f"Comando: wg set wg0 listen-port {peer_listen_port} private-key <(echo {private_key})")
        os.system(f"wg set wg0 listen-port {peer_listen_port} private-key <(echo {private_key})")
        
        os.system("ip link set up dev wg0")
    else:
        print("Sistema operativo no soportado.")
    
def get_wg_state():
    """Obtiene el estado de Wireguard.
    """
    print("Obteniendo estado de Wireguard...")
    os.system("wg show wg0")    
    
def get_wg_interface():
    """Obtiene la interfaz de Wireguard.
    """
    print("Obteniendo interfaz de Wireguard...")
    os.system("ip a show wg0")
    
def get_wg_interface_config():
    """Obtiene la configuración de la interfaz de Wireguard.
    """
    print("Obteniendo configuración de la interfaz de Wireguard...")
    os.system("wg showconf wg0")