import socket

client_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

IP=input("Enter IP_addres: ")
port=input("Enter Port number: ")

Port=int(port)



payload=input("Enter payload").encode('utf-8')
addr=(IP,Port)

client_socket.sendto(payload,addr)
data,addr=client_socket.recvfrom(1472)
print(str(data))
print("Client sending data to server  port  %s"%Port )

client_socket.close()