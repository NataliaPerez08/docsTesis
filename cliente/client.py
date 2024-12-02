from concurrent import futures
import grpc

protos, services = grpc.protos_and_services("auth.proto")


class Greeter(services.GreeterServicer):
    def SayHello(self, request, context):
        return  protos.HelloReply(message="Hello, %s!" % request.name)

class AuthService(services.AuthServiceServicer):
    def Register(self, request, context):
        return protos.RegisterRequest(message="Register email  %s" % request.email)

def serve():
    # Crear un servidor gRPC con 10 hilos. Con un canal inseguro para recibir las solicitudes del wrapper
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    # Agregar el servicio al servidor
    services.add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port('[::]:3041')
    server.start()
    print("Server running on port 3041")
    server.wait_for_termination()


def create_channel():
    # Leer el certificado del servidor (el certificado autofirmado)
    with open('./certs/localhost.crt', 'rb') as f:
        trusted_cert = f.read()
    # Crear las credenciales SSL usando el certificado del servidor
    credentials = grpc.ssl_channel_credentials(root_certificates=trusted_cert)
    # Crear un canal seguro para la comunicación con el servidor
    #with grpc.secure_channel('localhost:50051', credentials) as channel:

        # Crear el stub para hacer la llamada RPC
       #stub = auth_pb2_grpc.AuthServiceStub(channel)

        #try:
            # Realizar la solicitud
        #    response = stub.Authenticate(auth_pb2.AuthRequest(username='user', password='pass'))
           #   print("Token recibido:", response.token)
        #except grpc.RpcError as e:
            #   print(f"gRPC error: {e.code()} - {e.details()}")

if __name__ == '__main__':
    serve()
