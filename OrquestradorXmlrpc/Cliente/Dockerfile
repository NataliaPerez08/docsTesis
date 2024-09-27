# Usa una imagen base oficial de Python
FROM python:3.9-slim

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar todos los archivos de la carpeta 'src' a la imagen Docker de forma recursiva
COPY ./src /app

# Instalar las dependencias desde requirements.txt (si existe) COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Comando por defecto para ejecutar la aplicación
CMD ["python", "main.py"]
