import xmlrpc.client

# My serverd
dir_local = "http://0.0.0.0:3041/"

proxy = xmlrpc.client.ServerProxy(dir_local)

# Conexion con el servidor
print("Conectando con el servidor...")

print("Saludando al servidor...")
print(proxy.say_hello())

print("Registrando usuario...")
print(proxy.register_user("Juan", "juan@example", "1234"))



