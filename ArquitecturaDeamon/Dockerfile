# Crear una imagen de debian 
FROM debian:latest

# Instalar git
RUN apt-get update && apt-get install -y git

# Instalar wireguard
RUN apt-get install -y wireguard

# Clonar el repositorio
RUN git clone https://github.com/NataliaPerez08/docsTesis.git

# Copiar el archivo de configuración
COPY /docsTesis/ArquitecturaDeamon/wg0.conf /etc/wireguard/wg0.conf

# Iniciar el servicio
CMD ["wg-quick", "up", "wg0"]

# Exponer el puerto
EXPOSE 51820/udp

# Comando para ejecutar el contenedor
# docker build -t wireguard .