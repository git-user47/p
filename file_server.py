import socket
import os
import threading

s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.bind(('127.0.0.1',5000))

pid=os.getpid()
pid=str(pid)

def send_file(filename,addr):
    if os.path.isfile(filename):
        f=open(filename,'r')
        content=f.read()
        f.close()

        message="PID : "+pid+"\nContent\n"+content
    else:
        message="PID : "+pid+"\nFile doesn't exist"

    s.sendto(message.encode(),addr)
    print(message)

print("server is waiting...")

while True:
    data,addr=s.recvfrom(1024)
    filename=data.decode()

    t=threading.Thread(target=send_file,args=(filename,addr))
    t.start()
    
