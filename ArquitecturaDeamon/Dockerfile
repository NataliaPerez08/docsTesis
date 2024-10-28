# Crear una imagen de debian 
FROM debian:latest

# Instalar git
RUN apt-get update && apt-get install -y git

# Instalar python3
RUN apt-get install -y python3

# Instalar scapy
# Instalar librerias de python
RUN apt-get install -y python3-aioxmlrpc 

# Instalar scapy
RUN apt-get install -y python3-scapy

# Instalar wireguard
RUN apt-get install -y wireguard

# Clonar el repositorio
RUN git clone https://github.com/NataliaPerez08/docsTesis.git

# Entrar al directorio ArquitecturaDeamon/Cliente
WORKDIR /docsTesis/ArquitecturaDeamon/Cliente   

# Iniciar el servidor en ArquitecturaDeamon/Cliente/client-as-deamon.py
CMD ["python3", "client-as-deamon.py"]

# Exponer el puerto
EXPOSE 51820/udp
