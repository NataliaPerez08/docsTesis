import socket

# Create a UDP socket
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to a specific IP address and port
server_address = ('localhost', 12345)
udp_socket.bind(server_address)

while True:
    # Receive data from the socket
    data, address = udp_socket.recvfrom(1024)
    # Print the received message
    print(f"Received message: {data.decode()}")

    if data == None:
        break


# Close the socket
udp_socket.close()