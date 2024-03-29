import socket
import threading
import os

class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host, self.port))
        self.files_directory = "server_files"
        self.create_files_directory()

    def create_files_directory(self):
        if not os.path.exists(self.files_directory):
            os.makedirs(self.files_directory)

    def start(self):
        self.server_socket.listen(5)
        print(f"Server is running on {self.host}:{self.port}")

        while True:
            conn, addr = self.server_socket.accept()
            client_handler = threading.Thread(target=self.handle_client, args=(conn,))
            client_handler.start()

    def handle_client(self, conn):
        print('handle_client start')
        print(f"Connection from {conn.getpeername()}")
        command = conn.recv(1024).decode("utf-8")
        # if command == "LIST_FILES":
        #     self.send_file_list(conn)
        # else:
            # self.send_invalid_command_response(conn)
        filepath = os.path.join(self.files_directory, command)
        with open(filepath, "rb") as file:
            filedata = file.read(1024)
            while filedata:
                conn.send(filedata)
                filedata = file.read(1024)
        print(f"Sent {command} to {conn.getpeername()}")
        print('handle_client end')    
        conn.close()

    # def send_file_list(self, conn):
    #     print('send_file_list start')
    #     files = os.listdir(self.files_directory)
    #     file_list = ",".join(files)
    #     conn.send(file_list.encode("utf-8"))
    #     print('send_file_list end')

    def send_file(self, conn, filename):
        print('send_file start')
        file = open(filename, 'rb')
        filedata = file.read(1024)
        print(filedata)
        conn.send(filedata)
        print("Data has been transmitted successfully")
        print('send_file_list end')

if __name__ == "__main__":
    host = "127.0.0.1"
    port = 8080

    server = Server(host, port)
    server.start()
