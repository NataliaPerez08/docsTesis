# Crear una imagen de debian 
FROM debian:latest

# Instalar git
RUN apt-get update && apt-get install -y git

# Instalar python3
RUN apt-get install -y python3

# Instalar flask
RUN apt-get install -y python3-flask

# Instalar wireguard
RUN apt-get install -y wireguard

# Exponer el puerto 80 
EXPOSE 80