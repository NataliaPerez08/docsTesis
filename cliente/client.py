import requests

# URL del servidor
url = 'http://localhost:5000/api/data'

# Realizar una solicitud GET al servidor
response = requests.get(url)
if response.status_code == 200:
    print("GET Response:", response.json())

# Datos de ejemplo para enviar al servidor con POST
data_to_send = {"client_message": "Hello from the client!"}

# Realizar una solicitud POST al servidor
response = requests.post(url, json=data_to_send)
if response.status_code == 200:
    print("POST Response:", response.json())
