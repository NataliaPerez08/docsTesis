import grpc
from concurrent import futures
from google.auth.transport import requests
from google.oauth2 import id_token
from grpc import ServicerContext

# Cargar clases generadas por grpcio-tools
protos, services = grpc.protos_and_services("your_service.proto")

# Configuración del servidor
ALLOWED_AUDIENCE = "your-client-id.apps.googleusercontent.com"

# Función para verificar el token
def validate_token(context: ServicerContext):
    # Extraer el token del encabezado de autorización
    metadata = context.invocation_metadata()
    for key, value in metadata:
        if key == "authorization":
            token = value.split("Bearer ")[-1]  # Formato esperado: "Bearer <token>"
            break
    else:
        context.abort(grpc.StatusCode.UNAUTHENTICATED, "Missing authorization token")

    try:
        # Validar el token usando Google OAuth
        request_adapter = requests.Request()
        id_info = id_token.verify_oauth2_token(token, request_adapter, ALLOWED_AUDIENCE)

        # Validar información adicional si es necesario
        if "email" not in id_info:
            context.abort(grpc.StatusCode.UNAUTHENTICATED, "Invalid token payload")

        return id_info  # Retorna la información del token (ejemplo: email, roles, etc.)
    except ValueError as e:
        context.abort(grpc.StatusCode.UNAUTHENTICATED, f"Invalid token: {str(e)}")

# Implementación del servicio
class YourService(services.YourServiceServicer):
    def YourMethod(self, request, context):
        # Validar token
        user_info = validate_token(context)
        print(f"Authenticated user: {user_info['email']}")

        # Implementa la lógica de tu método aquí
        response = YourResponse(message="Hello, authenticated user!")
        return response

# Configurar y arrancar el servidor gRPC
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    # Agregar el servicio al servidor
    services.add_YourServiceServicer_to_server(YourService(), server)

    # Habilitar TLS si es necesario
    with open("./certs/localhost.key", "rb") as f:
        private_key = f.read()
    with open("./certs/localhost.crt", "rb") as f:
        certificate_chain = f.read()

    server_credentials = grpc.ssl_server_credentials(
        [(private_key, certificate_chain)]
    )

    server.add_secure_port("[::]:50051", server_credentials)

    # Arrancar el servidor
    server.start()
    print("Server is running on port 50051")
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
