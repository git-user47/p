import socket
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#connect to server with ip address and port number
s.connect(('127.0.0.1',5000))

#read the order of matrix
n=int(input("Enter the order of the matrix : "))

#create an empty list to store the matrix
matrix=[]

for i in range(n):
    row=list(map(int,input().split()))
    matrix.append(row)

print("Matrix is :",matrix)

#convert matrix to string to send to server
data=str(matrix)

#send matrix to server
s.send(data.encode())

result=s.recv(1024).decode()
print("The matrix is ",result)

s.close()



