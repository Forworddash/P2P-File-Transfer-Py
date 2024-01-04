import tkinter as tk
import socket

class ClientUI:
    def __init__(self, master):
        self.master = master
        master.title("Client")

        self.label = tk.Label(master, text="Enter server hostname:")
        self.label.pack()

        self.hostname_entry = tk.Entry(master)
        self.hostname_entry.pack()

        self.connect_button = tk.Button(master, text="Connect", command=self.connect_to_server)
        self.connect_button.pack()

        self.status_label = tk.Label(master, text="")
        self.status_label.pack()

        self.filename_label = tk.Label(master, text="Enter filename for incoming file:")
        self.filename_label.pack()

        self.filename_entry = tk.Entry(master)
        self.filename_entry.pack()

        self.receive_button = tk.Button(master, text="Receive File", command=self.receive_file)
        self.receive_button.pack()

        self.quit_button = tk.Button(master, text="Quit", command=master.quit)
        self.quit_button.pack()

        self.server_socket = None

    def connect_to_server(self):
        host = self.hostname_entry.get()
        port = 8080
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            self.server_socket.connect((host, port))
            self.status_label.config(text="Connected to the server.")
        except Exception as e:
            self.status_label.config(text=f"Connection failed: {str(e)}")

    def receive_file(self):
        if self.server_socket:
            filename = self.filename_entry.get()
            file = open(filename, 'wb')
            file_data = self.server_socket.recv(1024)
            file.write(file_data)
            file.close()
            self.status_label.config(text="File received successfully.")
        else:
            self.status_label.config(text="Not connected to the server.")

if __name__ == "__main__":
    root = tk.Tk()
    client_ui = ClientUI(root)
    root.mainloop()
