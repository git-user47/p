import socket
import threading

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.bind(('127.0.0.1',5000))

s.listen()

clients=[]

def handle_client(conn,addr):
    name=conn.recv(1024).decode()
    print(name," connected")

    while True:
        try:
            message=conn.recv(1024).decode()
            message=name + " : "+ message
            print(message)

            if not message or message=="exit":
                break

            for client in clients:
                if client!=conn:
                    client.send(message.encode())
        except:
            break 

        if conn==client:
            clients.remove(conn)  

while True:
    conn,addr=s.accept()

    clients.append(conn)

    t=threading.Thread(target=handle_client,args=(conn,addr))
    t.start()