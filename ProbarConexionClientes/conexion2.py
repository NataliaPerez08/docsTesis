import socket

def verificar_conectividad(direccion_ip, puerto):
    try:
        # Intenta crear un socket para establecer una conexión
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(2)  # Establece un tiempo de espera de 2 segundos

        # Intenta conectar al dispositivo en la dirección IP y puerto especificados
        s.connect((direccion_ip, puerto))

        print(f"Conectividad exitosa con {direccion_ip} en el puerto {puerto}")
        s.close()  # Cierra el socket después de establecer la conexión
    except Exception as e:
        print(f"No se pudo establecer la conexión con {direccion_ip} en el puerto {puerto}: {e}")

# Dirección IP y puerto del dispositivo de destino
direccion_ip_destino = '34.30.103.249'
puerto_destino = 80  # Puedes cambiar el puerto según el servicio que desees verificar

verificar_conectividad(direccion_ip_destino, puerto_destino)
