import xmlrpc.client
import ipaddress

with xmlrpc.client.ServerProxy("http://localhost:8000/") as proxy:
    print("100 is even: %s" % str(proxy.is_even(100))) 

    opcion = ""
    while True:
        print("1. Crear Red Privada 2. Ver Redes Privadas 3. Salir")
        opcion = input("Opción: ")

        if opcion == "1":
            input_name = input("Nombre de la red: ")
            private_network_id = proxy.create_private_network(input_name)
            print(f"Private network ID: {private_network_id}")

        elif opcion == "2":
            print("Private networks:")
            print(proxy.get_private_networks())
        elif opcion == "3":
            break
        pass
