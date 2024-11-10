import grpc
from concurrent import futures
import jwt  # PyJWT
import auth_pb2
import auth_pb2_grpc
import ssl

SECRET_KEY = "your_secret_key"

class AuthService(auth_pb2_grpc.AuthServiceServicer):
    def Authenticate(self, request, context):
        if request.username == "user" and request.password == "pass":
            #token = jwt.encode({"user": request.username}, SECRET_KEY, algorithm="HS256")
            return 1#auth_pb2.AuthResponse(token=token)
        #context.abort(grpc.StatusCode.UNAUTHENTICATED, "Invalid credentials")

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    auth_pb2_grpc.add_AuthServiceServicer_to_server(AuthService(), server)

    # Cargar los certificados autofirmados
    with open('./certs/localhost.key', 'rb') as f:
        private_key = f.read()
    with open('./certs/localhost.crt', 'rb') as f:
        certificate_chain = f.read()

    # Crear las credenciales SSL para el servidor
    server_credentials = grpc.ssl_server_credentials(((private_key, certificate_chain),))

    # Escuchar en un puerto seguro
    server.add_secure_port('[::]:50051', server_credentials)
    server.start()
    print("Server running with SSL on port 50051")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()