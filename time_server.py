import socket
import threading
from datetime import datetime

s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.bind(('127.0.0.1',5000))

def get_time(addr):
    current_time=str(datetime.now())
    s.sendto(current_time.encode(),addr)
    print("Time send to client address : ",addr)

print("Waiting for client requests...")

while True:
    data,addr=s.recvfrom(1024)
    t=threading.Thread(target=get_time, args=(addr,))
    t.start()