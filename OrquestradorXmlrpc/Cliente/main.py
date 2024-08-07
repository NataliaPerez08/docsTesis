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
# python3 main.py crear_endpoint <id_red_privada> <nombre_endpoint>
# python3 main.py ver_endpoints <id_red_privada>
# python3 main.py conectar_endpoint <id_endpoint> <id_red_privada>
# python3 main.py conectar_endpoint_directo <ip_wg_endpoint> <puerto_wg_endpoint>

# python3 main.py obtener_configuracion_wireguard_local
# python3 main.py obtener_configurarion_wireguard_servidor

# python3 main.py prueba_wg_conf
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
        
    # Comando no reconocido
    else:
        print("Comando no reconocido")
        sys.exit()
