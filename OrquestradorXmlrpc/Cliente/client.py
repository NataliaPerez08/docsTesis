import xmlrpc.client
import ipaddress

from conn_scapy import verificar_conectividad

with xmlrpc.client.ServerProxy("http://localhost:8000/") as proxy:
    opcion = ""
    while True:
        print("1. Crear Red Privada "+
              "2. Ver Redes Privadas "+ 
              "3. Crear Endpoint "+
              "4. Ver Endpoints "+
              "5. Conectar a endpoint "+
              "6. Salir")
        opcion = input("Opción: ")

        if opcion == "1":
            print("Creando red privada...")
            input_name = input("Nombre de la red: ")
            private_network_id = proxy.create_private_network(input_name)
            print(f"ID de la red privada: {private_network_id}")
            
        elif opcion == "2":
            print("Ver Redes Privadas:")
            print(proxy.get_private_networks())

        elif opcion == "3":
            print("Crear endpoins:")
            private_network_id = input("ID de la red privada: ")
            endpoint_name = input("Nombre del endpoint: ")
            endpoint_id = proxy.create_endpoint(private_network_id, endpoint_name)
            print("Endpoint creado con ID: ", endpoint_id)
            
        elif opcion == "4":
            print("Ver Endpoints:")
            private_network_id = input("ID de la red privada: ")
            print(proxy.get_endpoints(private_network_id))

        elif opcion == "5":
            private_network_id = input("ID de la red privada: ")
            endpoint_ip = input("Endpoint: ")
            verificar_conectividad(endpoint_ip)
            # Si la conexion es por relay- INDIRECTA
            #proxy.connect_to_private_network(private_network_id, endpoint_ip)
            print("Conectado a la red privada")

        elif opcion == "6":
            break
        pass
