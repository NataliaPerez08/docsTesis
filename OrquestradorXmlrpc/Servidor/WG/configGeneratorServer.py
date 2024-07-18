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
        

def create_wg_interface(ip_wg, public_key, private_key, peer_public_key=None, peer_allowed_ips=None, peer_endpoint_ip=None, peer_listen_port=None):
    """Crea una interfaz de Wireguard.
    """
    print("Creando interfaz...")
    # Si es Linux
    if os.name == "posix":
        # Verificar si existe la interfaz
        if os.system("ip link show wg10") == 0:
            print("La interfaz ya existe.")
        else:     
            os.system(f"ip link add dev wg10 type wireguard")
            os.system(f"ip address add {ip_wg} dev wg10")
            
        # Configurar la interfaz con las llaves  pública y privada
        os.system(f"wg set wg10 private-key <(echo {private_key})")
        os.system(f"wg set wg10 listen-port 51820")
        if peer_public_key is not None and peer_allowed_ips is not None and peer_endpoint_ip is not None and peer_listen_port is not None:
            os.system(f"wg set wg10 peer {peer_public_key} allowed-ips {peer_allowed_ips} endpoint {peer_endpoint_ip}:{peer_listen_port}")
        
        
        os.system("ip link set up dev wg10")
    else:
        print("Sistema operativo no soportado.")
    
def get_wg_state():
    """Obtiene el estado de Wireguard.
    """
    print("Obteniendo estado de Wireguard...")
    os.system("wg show wg10")    
    
def get_wg_interface():
    """Obtiene la interfaz de Wireguard.
    """
    print("Obteniendo interfaz de Wireguard...")
    os.system("ip a show wg10")
    
def get_wg_interface_config():
    """Obtiene la configuración de la interfaz de Wireguard.
    """
    print("Obteniendo configuración de la interfaz de Wireguard...")
    os.system("wg showconf wg10")