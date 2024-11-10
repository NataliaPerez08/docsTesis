import grpc
import auth_pb2
import auth_pb2_grpc

def run():
    # Leer el certificado del servidor (el certificado autofirmado)
    with open('./certs/localhost.crt', 'rb') as f:
        trusted_cert = f.read()

    # Crear las credenciales SSL usando el certificado del servidor
    credentials = grpc.ssl_channel_credentials(root_certificates=trusted_cert)

    # Crear un canal seguro para la comunicación con el servidor
    with grpc.secure_channel('localhost:50051', credentials) as channel:
        # Crear el stub para hacer la llamada RPC
        stub = auth_pb2_grpc.AuthServiceStub(channel)
        
        try:
            # Realizar la solicitud
            response = stub.Authenticate(auth_pb2.AuthRequest(username='user', password='pass'))
            print("Token recibido:", response.token)
        except grpc.RpcError as e:
            print(f"gRPC error: {e.code()} - {e.details()}")

if __name__ == '__main__':
    run()
