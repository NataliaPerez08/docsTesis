import grpc
from google.auth.transport.requests import Request
from google.oauth2 import service_account
from google.auth.transport.grpc import AuthMetadataPlugin
from grpc import metadata_call_credentials, ssl_channel_credentials

# Archivo de credenciales de la cuenta de servicio
#SERVICE_ACCOUNT_FILE = "path/to/service-account.json"
#SCOPES = ["https://www.googleapis.com/auth/cloud-platform"]

# Cargar las credenciales
credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES
)

# Actualizar el token si es necesario
credentials.refresh(Request())

# Crear el plugin de autenticación gRPC
auth_metadata_plugin = AuthMetadataPlugin(
    lambda context, callback: callback((("authorization", f"Bearer {credentials.token}"),), None)
)

# Configurar las credenciales gRPC
call_credentials = metadata_call_credentials(auth_metadata_plugin)

# Configurar el canal seguro
with open("./certs/localhost.key", "rb") as f:
    server_cert = f.read()

ssl_credentials = ssl_channel_credentials(server_cert)
composite_credentials = grpc.composite_channel_credentials(ssl_credentials, call_credentials)

# Conectar al servidor gRPC
channel = grpc.secure_channel("your-grpc-server-endpoint:443", composite_credentials)

# Cargar y usar el cliente gRPC generado
from your_grpc_module import YourServiceStub, YourRequest  # Generado por grpcio-tools

stub = YourServiceStub(channel)
request = YourRequest(param="value")
response = stub.YourMethod(request)
print(response)

