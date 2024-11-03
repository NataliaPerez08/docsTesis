# Usa una imagen base de Python
FROM python:3.10-slim

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia el archivo de servidor y los certificados
COPY server.py .
COPY certs/server.crt certs/server.key certs/

# Instala Flask y Flask-JWT-Extended sin pip
RUN pip install Flask
RUN pip install Flask-JWT-Extended

# Expone el puerto 5000 para el servidor Flask
EXPOSE 5000

# Comando para ejecutar el servidor
CMD ["python", "server.py"]
