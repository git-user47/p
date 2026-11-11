import socket
import os
import threading

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

filename=input()
s.sendto(filename.encode(),(('127.0.0.1',5000)))

data,addr=s.recvfrom(65507)
content=data.decode()
print(content)