import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('127.0.0.1', 12333)


message = "Hey I'm the Client".encode('utf-8')
client_socket.sendto(message, server_address)
        
data, addr = client_socket.recvfrom(1024)  # buffer size is required

print("Received from server:", data.decode('utf-8'))

client_socket.close()
