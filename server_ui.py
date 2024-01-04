import socket
import threading
import tkinter as tk
from server_ui import ServerUI

class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host, self.port))
        self.server_ui = None

    def start(self):
        self.server_ui = ServerUI()  # Create an instance of ServerUI
        self.server_ui.start()  # Start the Tkinter main loop in a separate thread
        self.server_socket.listen(1)
        print(self.host)
        print('waiting for incoming connections...')

        conn, addr = self.server_socket.accept()
        print(addr, "has connected to the server")

        filename = self.server_ui.get_filename()  # Get the filename from the UI
        self.send_file(conn, filename)

    def send_file(self, conn, filename):
        file = open(filename, 'rb')
        filedata = file.read(1024)
        print(filedata)
        conn.send(filedata)
        print("Data has been transmitted successfully")

if __name__ == "__main__":
    host = "127.0.0.1"
    port = 8080

    server = Server(host, port)
    server.start()
