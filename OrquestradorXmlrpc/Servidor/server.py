from xmlrpc.server import SimpleXMLRPCServer

# Mis clases
import OrquestradorXmlrpc.Servidor.RedPrivada as rp

def is_even(n):
    return n % 2 == 0

def create_private_network():
    print("Creating private network...")
    red = rp.RedPrivada("Red1")
    return red.identificador

server = SimpleXMLRPCServer(("localhost", 8000))
print("Listening on port 8000...")
server.register_function(is_even, "is_even")
server.serve_forever()