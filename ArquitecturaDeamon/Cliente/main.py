# Configurador CLI
import xmlrpc.client
import sys
import os

# My serverd
dir_local = "http://0.0.0.0:3041/"

deamon = xmlrpc.client.ServerProxy(dir_local)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python3 main.py <comando> <argumentos>")
        sys.exit()
    comando = sys.argv[1]
    
    # python3 main.py registrar_usuario <nombre> <email> <password>
    if comando == "registrar_usuario":
        if len(sys.argv) != 5:
            print("Uso: python3 main.py registrar_usuario <nombre> <email> <password>")
            sys.exit()
        result = deamon.register_user(sys.argv[2], sys.argv[3], sys.argv[4])
        if result:
            print("Usuario registrado!")
        else:
            print("Error al registrar el usuario! El correo ya esta registrado")

    # python3 main.py identificar_usuario <email> <password>    
    elif comando == "identificar_usuario":
        if len(sys.argv) != 4:
            print("Uso: python3 main.py identificar_usuario <email> <password>")
            sys.exit()
        result = deamon.identify_me(sys.argv[2], sys.argv[3])
        if result:
            print("Usuario identificado!")
    
    # python3 main.py whoami
    elif comando == "whoami":
        print(deamon.whoami())

    # python3 main.py crear_red_privada <nombre>
    elif comando == "crear_red_privada":
        if len(sys.argv) != 3:
            print("Uso: python3 main.py crear_red_privada <nombre>")
            sys.exit()
        deamon.create_private_network(sys.argv[2])

    # python3 main.py ver_redes_privadas
    elif comando == "ver_redes_privadas":
        result = deamon.get_private_networks()
        print(result)

    # python3 main.py ver_endpoints <id_red_privada>
    elif comando == "ver_endpoints":
        if len(sys.argv) != 3:
            print("Uso: python3 main.py ver_endpoints <id_red_privada>")
            sys.exit()
        deamon.ver_endpoints(sys.argv[2])

    # python3 main.py conectar_endpoint <id_endpoint> <id_red_privada>
    elif comando == "conectar_endpoint":
        # Este comando pregunta al servidor si el endpoint esta conectado y comparte su
        # configuraracion. Le permite conectarse con relaying
        if len(sys.argv) != 4:
            print("Uso: python3 main.py conectar_endpoint <id_endpoint> <id_red_privada>")
            sys.exit()
        deamon.conectar_endpoint(sys.argv[2], sys.argv[3])

    # python3 main.py conectar_endpoint_directo <ip_wg_endpoint> <puerto_wg_endpoint>
    elif comando == "conectar_endpoint_directo":
        if len(sys.argv) != 4:
            print("Uso: python3 main.py conectar_endpoint_directo <ip_wg_endpoint> <puerto_wg_endpoint>")
            sys.exit()
        deamon.conectar_endpoint_directo(sys.argv[2], sys.argv[3])

    # python3 main.py obtener_clave_publica_servidor
    elif comando == "obtener_clave_publica_servidor":
        deamon.obtener_clave_publica_servidor()

    # python3 main.py obtener_configuracion_wireguard_local
    elif comando == "obtener_configuracion_wireguard_local":
        # Verificar si el comando se ejecuto como administrador en Linux
        if os.geteuid() != 0:
            print("Se necesita permisos de administrador para ejecutar el comando")
            sys.exit()
        else:
            deamon.obtener_configuracion_wireguard_local()

    # python3 main.py obtener_configuracion_wireguard_servidor
    elif comando == "obtener_configuracion_wireguard_servidor":
        deamon.obtener_configuracion_wireguard_servidor()
        
    
    # Si el cliente tiene ip publica debe ser incluida en la configuracion
    # python3 main.py añadir_ip_publica <ip>
    elif comando == "añadir_ip_publica":
        if len(sys.argv) != 3:
            print("Uso: python3 main.py añadir_ip_publica <ip>")
            sys.exit()
        deamon.add_public_ip(sys.argv[2])
        
    # Consultar el ip registrada del cliente
    # python3 main.py consultar_ip_publica_cliente
    elif comando == "consultar_ip_publica_cliente":
        ip = deamon.get_public_ip()
        print(f"La ip publica del cliente es: {ip}")
        
    # Configurar el cliente como peer. Dado que tiene una ip publica
    # python3 main.py registrar_como_peer <nombre> <id_red_privada> <ip_cliente> <puerto_cliente>
    elif comando == "registrar_como_peer":
        # Verificar si el comando se ejecuto como administrador en Linux
        if os.geteuid() != 0:
            print("Se necesita permisos de administrador para ejecutar el comando")
            sys.exit()
            
        if len(sys.argv) != 6:
            print("Uso: python3 main.py registrar_como_peer <nombre> <id_red_privada> <ip_cliente> <puerto_cliente>")
            sys.exit()
        deamon.configure_as_peer(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])
        
    # python3 main.py obtener_clave_publica_cliente
    elif comando == "obtener_clave_public_cliente":
        my_public_key = deamon.get_client_public_key()
        print(f"La clave publica del cliente es: {my_public_key}")
        
    # Crear un peer en el servidor
    # python3 main.py iniciar_interfaz_wireguard <ip_cliente>
    elif comando == "iniciar_interfaz_wireguard":
        # Verificar si el comando se ejecuto como administrador en Linux
        if os.geteuid() != 0:
            print("Se necesita permisos de administrador para ejecutar el comando")
            sys.exit()
        else:
            if len(sys.argv) != 3:
                print("Uso: python3 main.py iniciar_interfaz_wireguard <ip_cliente>")
                sys.exit()
                
            deamon.init_wireguard_interface(sys.argv[2])

    # python3 main.py  crear_peer <public_key> <allowed_ips> <ip_cliente> <listen_port>
    elif comando == "crear_peer":
        if len(sys.argv) != 6:
            print("Uso: python3 main.py  crear_peer <public_key> <allowed_ips> <ip_cliente> <listen_port>")
            sys.exit()
        deamon.register_peer(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])
    
    # python3 cerrar_sesion
    elif comando == "cerrar_sesion":
        if deamon.cerrar_sesion():
            print("Se cerro la sesion")

    # Comando no reconocido
    else:
        print("Comando no reconocido")
        sys.exit()