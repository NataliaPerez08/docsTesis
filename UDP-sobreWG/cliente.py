import socket

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Send data to server
server_address = ('10.0.0.2', 80)
message = 'Hello, server!'
sock.sendto(message.encode(), server_address)

while True:
    input_data = input("Enter message: ")
    if input_data == "exit":
        break
    sock.sendto(input_data.encode(), server_address)

# Close the socket
sock.close()