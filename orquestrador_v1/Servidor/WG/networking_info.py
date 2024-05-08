import os
import subprocess
def recupera_iptables():
    print("Recuperando regras de iptables")
    # Recupera as regras de iptables
    # iptables -L -n -v
    ip_tables = subprocess.run(["iptables", "-L"], stdout=subprocess.PIPE)
    print(ip_tables.stdout.decode())
    return ip_tables.stdout.decode()

def ipaddr(nombre_interfaz):
    # Recupera información de la interfaz de red 
    # ip addr show nombre_interfaz
    ip_addr = subprocess.run(["ip", "addr", "show", nombre_interfaz], stdout=subprocess.PIPE)
    print(ip_addr.stdout.decode())
    return ip_addr.stdout.decode()