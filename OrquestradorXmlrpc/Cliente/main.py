from Cliente import Cliente
import sys
import os
# Manejo por linea de comandos
# python3 main.py registrar_usuario <nombre> <email> <password>
# python3 main.py identificar_usuario <email> <password>
# python3 main.py whoami
# python3 main.py obtener_clave_publica_servidor
# python3 main.py cerrar_sesion


# python3 main.py crear_red_privada <nombre>
# python3 main.py ver_redes_privadas
# python3 main.py ver_endpoints <id_red_privada>
# python3 main.py conectar_endpoint <id_endpoint> <id_red_privada>
# python3 main.py conectar_endpoint_directo <ip_wg_endpoint> <puerto_wg_endpoint>

# python3 main.py obtener_clave_publica_cliente

# python3 main.py obtener_configuracion_wireguard_local
# python3 main.py obtener_configurarion_wireguard_servidor

# python3 main.py añadir_ip_publica <ip>
# python3 main.py consultar_ip_publica
# python3 main.py init_wireguard_interface
# python3 main.py registrar_como_peer <nombre> <id_red_privada> <ip_cliente> <puerto_cliente> 
# python3 main.py  crear_peer <public_key> <allowed_ips> <ip_cliente> <listen_port> <ip_servidor>



if __name__ == "__main__":
    main = Cliente()
    
    if len(sys.argv) < 2:
        print("Uso: python3 main.py <comando> <argumentos>")
        sys.exit()
    comando = sys.argv[1]

    if comando == "registrar_usuario":
        if len(sys.argv) != 5:
            print("Uso: python3 main.py registrar_usuario <nombre> <email> <password>")
            sys.exit()
        main.register_user(sys.argv[2], sys.argv[3], sys.argv[4])
        
    elif comando == "identificar_usuario":
        if len(sys.argv) != 4:
            print("Uso: python3 main.py identificar_usuario <email> <password>")
            sys.exit()
        main.identify_me(sys.argv[2], sys.argv[3])
        
    elif comando == "whoami":
        print(main.whoami())

    elif comando == "crear_red_privada":
        if len(sys.argv) != 3:
            print("Uso: python3 main.py crear_red_privada <nombre>")
            sys.exit()
        main.create_private_network(sys.argv[2])

    elif comando == "ver_redes_privadas":
        main.get_private_networks()

    elif comando == "crear_endpoint":
        if len(sys.argv) != 4:
            print("Uso: python3 main.py crear_endpoint <id_red_privada> <nombre_endpoint>")
            sys.exit()
            
        # Verificar si el comando se ejecuto como administrador en Linux  
        if os.geteuid() != 0:
            print("Se necesita permisos de administrador para ejecutar el comando")
            sys.exit()
        else:
            main.crear_endpoint(sys.argv[2], sys.argv[3])

    elif comando == "ver_endpoints":
        if len(sys.argv) != 3:
            print("Uso: python3 main.py ver_endpoints <id_red_privada>")
            sys.exit()
        main.ver_endpoints(sys.argv[2])

    elif comando == "conectar_endpoint":
        if len(sys.argv) != 4:
            print("Uso: python3 main.py conectar_endpoint <id_endpoint> <id_red_privada>")
            sys.exit()
        main.conectar_endpoint(sys.argv[2], sys.argv[3])

    elif comando == "conectar_endpoint_directo":
        if len(sys.argv) != 4:
            print("Uso: python3 main.py conectar_endpoint_directo <ip_wg_endpoint> <puerto_wg_endpoint>")
            sys.exit()
        main.conectar_endpoint_directo(sys.argv[2], sys.argv[3])

    elif comando == "obtener_clave_publica_servidor":
        main.obtener_clave_publica_servidor()

    elif comando == "obtener_configuracion_wireguard_local":
        # Verificar si el comando se ejecuto como administrador en Linux
        if os.geteuid() != 0:
            print("Se necesita permisos de administrador para ejecutar el comando")
            sys.exit()
        else:
            main.obtener_configuracion_wireguard_local()

    elif comando == "obtener_configuracion_wireguard_servidor":
        main.obtener_configuracion_wireguard_servidor()
        
    elif comando == "cerrar_sesion":
        main.cerrar_sesion()
    
    # Si el cliente tiene ip publica debe ser incluida en la configuracion
    elif comando == "añadir_ip_publica":
        if len(sys.argv) != 3:
            print("Uso: python3 main.py añadir_ip_publica <ip>")
            sys.exit()
        main.add_public_ip(sys.argv[2])
        
    # Consultar el ip registrada del cliente
    elif comando == "consultar_ip_publica":
        ip = main.get_public_ip()
        print(f"La ip publica del cliente es: {ip}")
        
    # Configurar el cliente como peer. Dado que tiene una ip publica
    # python3 main.py registrar_como_peer <nombre> <id_red_privada> <ip_cliente> <puerto_cliente>
    elif comando == "registrar_como_peer":
        # Verificar si el comando se ejecuto como administrador en Linux
        if os.geteuid() != 0:
            print("Se necesita permisos de administrador para ejecutar el comando")
            sys.exit()
            
        if len(sys.argv) != 7:
            print("Uso: python3 main.py registrar_como_peer <nombre> <id_red_privada> <ip_cliente> <puerto_cliente>")
            sys.exit()
        main.configure_as_peer(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])
        
        
    elif comando == "obtener_clave_publica_cliente":
        my_public_key = main.get_client_public_key()
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
                
            main.init_wireguard_interface(sys.argv[2])
        
    # Comando no reconocido
    else:
        print("Comando no reconocido")
        sys.exit()
