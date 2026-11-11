import socket

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

s.sendto("Time".encode(),(('127.0.0.1',5000)))

data,addr=s.recvfrom(1024)
print("Current time : ",data.decode())

s.close()