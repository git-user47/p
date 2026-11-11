import socket

s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.bind(('127.0.0.1',5000))

og,addr=s.recvfrom(1024)
og=og.decode()
print("Sentence from client : ",og)

abbr={"bro":"friend",
      "I'm" : "I am",
      "omy" : "on my way"
}

for short,full in abbr.items():
    og=og.replace(short,full)

print("Translated sentence : ",og)

s.sendto(og.encode(),addr)


s.close()