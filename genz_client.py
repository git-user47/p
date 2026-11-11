import socket
s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sentence=input("Enter a sentence : ")
s.sendto(sentence.encode(),(('127.0.0.1',5000)))

og,addr=s.recvfrom(1024)
print("Translated sentence : ",og.decode())

s.close()