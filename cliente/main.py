# Configurador CLI
# Descripción: Configurador de la interfaz de línea de comandos para el cliente
import grpc
import sys

# My serverd
dir_local = "http://0.0.0.0:3041/"
deamon = grpc.insecure_channel(dir_local)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python3 main.py <comando> <argumentos>")
        sys.exit()
    comando = sys.argv[1]

    if comando == "help":
        print("Comandos disponibles:")
        print("  registrar_usuario <nombre> <email> <password>")
        result = deamon.register_user(sys.argv[2], sys.argv[3], sys.argv[4])
        
    
    # python3 main.py register_user <nombre> <email> <password>
    if comando == "registrar_usuario":
        if len(sys.argv) != 5:
            print("Uso: python3 main.py registrar_usuario <nombre> <email> <password>")
            sys.exit()
        result = deamon.register_user(sys.argv[2], sys.argv[3], sys.argv[4])
        if result:
            print("Usuario registrado!")
        else:
            print("Error al registrar el usuario! El correo ya esta registrado")

    # Comando no reconocido
    else:
        print("Comando no reconocido")
        sys.exit()