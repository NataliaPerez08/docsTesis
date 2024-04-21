import os
import subprocess
def recupera_iptables():
    # Recupera as regras de iptables
    # iptables -L -n -v
    ip_tables = subprocess.run(["iptables", "-L", "-n", "-v"], stdout=subprocess.PIPE)
    return ip_tables.stdout.decode()