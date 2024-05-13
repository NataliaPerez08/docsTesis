import socket

def check_udp_port(host, port):
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.settimeout(1)  # Set a timeout for the connection attempt
    try:
        udp_socket.sendto(b'', (host, port))  # Send an empty UDP packet
        udp_socket.recvfrom(1024)  # Receive a response (if any)
        print(f"UDP port {port} is open on {host}.")
    except socket.timeout:
        print(f"UDP port {port} is closed on {host}.")
    finally:
        udp_socket.close()

# Example usage:
host = '192.168.2.1'
port = 12345
check_udp_port(host, port)