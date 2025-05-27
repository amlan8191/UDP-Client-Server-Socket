import socket

print("Server waiting for DGRAM")
message="Hello I'm a Server".encode('utf-8')
server_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server_socket.bind(('127.0.0.1',12345))
data,addr=server_socket.recvfrom(1472)
print(str(data))
server_socket.sendto(message,addr)