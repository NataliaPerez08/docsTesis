import xmlrpc.client
import sys
from conn_scapy import verificar_conectividad

with xmlrpc.client.ServerProxy("http://localhost:8000/") as proxy:
    # Manejo por linea de comandos
    # python3 client.py crear_red_privada
    # python3 client.py ver_redes_privadas
    # python3 client.py crear_endpoint
    # python3 client.py conectar_endpoint
    # python3 client.py salir
    opcion = sys.argv[1] 
    
    if opcion == "crear_red_privada":
        print("Creando red privada...")
        input_name = sys.argv[2]
        private_network_id = proxy.create_private_network(input_name)
        print(f"ID de la red privada: {private_network_id}")

    elif opcion == "ver_redes_privadas":
        print("Obteniendo redes privadas...")
        print(proxy.get_private_networks())

    elif opcion == "crear_endpoint":
        print("Creando endpoint...")
        private_network_id = sys.argv[2]
        endpoint_name = sys.argv[3]
        endpoint_id = proxy.create_endpoint(private_network_id, endpoint_name)
        print(f"ID del endpoint: {endpoint_id}")

    elif opcion == "conectar_endpoint":
        print("Conectando endpoint...")
        endpoint_id = sys.argv[2]
        private_network_id = sys.argv[3]
        endpoint = proxy.get_endpoint_by_id(endpoint_id)
        private_network = proxy.get_private_network_by_id(private_network_id)
        if endpoint is None or private_network is None:
            print("Endpoint o red privada no encontrados!")
        print(f"Endpoint: {endpoint}")
        print(f"Red privada: {private_network}")
        verificar_conectividad(endpoint.ip_addr, private_network.last_host_assigned)