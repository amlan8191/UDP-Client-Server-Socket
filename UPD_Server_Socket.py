import socket

server_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server_socket.bind(('127.0.0.1',12333))

while True:
    data,addr=server_socket.recvfrom(1024)
    print(str(data))
    message="Hello I'm UDP server".encode('utf-8')
    server_socket.sendto(message,addr)
