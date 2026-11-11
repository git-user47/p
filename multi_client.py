import socket
import threading

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.connect(('127.0.0.1',5000))

name=input("Enter your name : ")
s.send(name.encode())

def receive_message():
    while True:
        try:
            message=s.recv(1024).decode()
            print(message)
            if not message or message=="exit":
                break

        except:
            break

t=threading.Thread(target=receive_message)
t.start()

while True:
    message=input()
    if message=="exit":
        s.send(message.encode())
        break
    print("You : ",message)
    s.send(message.encode())

s.close()