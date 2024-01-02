import socket

s = socket.socket()
host = socket.gethostname()
port = 8080
s.bind((host, port))
s.listen(1)
print(host)
print('waiting for incoming connections...')

conn, addr = s.accept()
print(addr, "Has connected to the server")



filename = input(str("Please enter the filename of the file : "))
file = open(filename, 'rb')
filedata = file.read(1024)
print(filedata)
conn.send(filedata)
print("Data has been transmitted successfully")