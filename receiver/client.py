import socket
s = socket.socket()
host = input(str("Please enter the hostname of the server : "))
port = 8080
s.connect((host, port))
print("Connected...")

filename = input(str("Please enter a filename for the incoming file : "))
file = open(filename, 'wb')
file_data = s.recv(1024)
file.write(file_data)
file.close()
print("File has been received successfully.")