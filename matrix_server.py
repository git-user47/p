import socket
import ast

#create tcp socket
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#bind
s.bind(('127.0.0.1',5000))

#listen for requests
s.listen(1)

print("Waiting for client reuests...")

#accept
conn,addr=s.accept()

print("Connection established with :",addr)

#receive the matrix from client
data=conn.recv(1024).decode()

#convert the string to matrix
matrix=ast.literal_eval(data)

print("The matrix received from client is ",matrix)

n=len(matrix)

upper=True
lower=True

for i in range(n):
    for j in range(n):
        if i>j and matrix[i][j]!=0:
            upper=False
        if i<j and matrix[i][j]!=0:
            lower=False

if upper and lower:
    result="a diagonal matrix"
elif upper:
    result="an upper triangular matrix"
elif lower:
    result="a lower triangular matrix"
else:
    result="neither upper nor lower triangular matrix"

print("Matrix is ",result)

#send result back to client
conn.send(result.encode())

#terminate connection
conn.close()

#close socket
s.close()
