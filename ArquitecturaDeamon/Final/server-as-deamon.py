# Client as deamon
from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler


# Servidor en la nube
dir_servidor="http://natalia-testing.online:80/"
dir_servidor="0.0.0.0"

# Servidor local
dir_local = "0.0.0.0"
port_local = 3041
wg_public_key = -1
wg_private_key = -1
wg_ip = -1
wg_port = -1

# Create server
xmlrpc_server = SimpleXMLRPCServer((dir_local,port_local),  logRequests=True)

def say_hello():
    return "Hello!"

def register_user(name, email, password):
    print(f"Registrando usuario: {name} {email} {password}")
    return True

def identify_user(email, password):
    print(f"Identificando usuario: {email} {password}")
    return True

def whoami():
    return "Juan"

def create_private_network(name):
    print(f"Creando red privada: {name}")
    return 1

def get_private_networks():
    return ["Red1", "Red2"]

def get_endpoints(id_red_privada):
    return [{"id":1, "ip":"0.0.0.0", "puerto":3042}]

# Register functions
xmlrpc_server.register_function(say_hello)
xmlrpc_server.register_function(register_user)
xmlrpc_server.register_function(identify_user)
xmlrpc_server.register_function(whoami)
xmlrpc_server.register_function(create_private_network)
xmlrpc_server.register_function(get_private_networks)

xmlrpc_server.serve_forever()