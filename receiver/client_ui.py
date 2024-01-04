# import tkinter as tk
# import socket

# class ClientUI:
#     def __init__(self, master):
#         self.master = master
#         master.title("Client")

#         self.label = tk.Label(master, text="Enter server hostname:")
#         self.label.pack()

#         self.hostname_entry = tk.Entry(master)
#         self.hostname_entry.pack()

#         self.connect_button = tk.Button(master, text="Connect", command=self.connect_to_server)
#         self.connect_button.pack()

#         self.status_label = tk.Label(master, text="")
#         self.status_label.pack()

#         self.filename_label = tk.Label(master, text="Enter filename for incoming file:")
#         self.filename_label.pack()

#         self.filename_entry = tk.Entry(master)
#         self.filename_entry.pack()

#         self.receive_button = tk.Button(master, text="Receive File", command=self.receive_file)
#         self.receive_button.pack()

#         self.quit_button = tk.Button(master, text="Quit", command=master.quit)
#         self.quit_button.pack()

#         self.server_socket = None

#     def connect_to_server(self):
#         host = self.hostname_entry.get()
#         port = 8080
#         self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#         try:
#             self.server_socket.connect((host, port))
#             self.status_label.config(text="Connected to the server.")
#         except Exception as e:
#             self.status_label.config(text=f"Connection failed: {str(e)}")

#     def receive_file(self):
#         if self.server_socket:
#             filename = self.filename_entry.get()
#             file = open(filename, 'wb')
#             file_data = self.server_socket.recv(1024)
#             file.write(file_data)
#             file.close()
#             self.status_label.config(text="File received successfully.")
#         else:
#             self.status_label.config(text="Not connected to the server.")

# if __name__ == "__main__":
#     root = tk.Tk()
#     client_ui = ClientUI(root)
#     root.mainloop()

# import tkinter as tk
# import socket

# class ClientUI:
#     def __init__(self, master):
#         self.master = master
#         master.title("Client")

#         self.label = tk.Label(master, text="Enter server hostname:")
#         self.label.pack()

#         self.hostname_entry = tk.Entry(master)
#         self.hostname_entry.pack()

#         self.connect_button = tk.Button(master, text="Connect", command=self.connect_to_server)
#         self.connect_button.pack()

#         self.status_label = tk.Label(master, text="")
#         self.status_label.pack()

#         self.file_listbox = tk.Listbox(master)
#         self.file_listbox.pack()

#         self.receive_button = tk.Button(master, text="Receive File", command=self.receive_file)
#         self.receive_button.pack()

#         self.quit_button = tk.Button(master, text="Quit", command=master.quit)
#         self.quit_button.pack()

#         self.server_socket = None

#     def connect_to_server(self):
#         host = self.hostname_entry.get()
#         port = 8080
#         self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#         try:
#             self.server_socket.connect((host, port))
#             self.status_label.config(text="Connected to the server.")
#             self.request_file_list()
#         except Exception as e:
#             self.status_label.config(text=f"Connection failed: {str(e)}")

#     def request_file_list(self):
#         self.server_socket.send(b"LIST_FILES")
#         file_list = self.server_socket.recv(1024).decode("utf-8")
#         files = file_list.split(",")
#         self.file_listbox.delete(0, tk.END)
#         for file in files:
#             self.file_listbox.insert(tk.END, file)

#     def receive_file(self):
#         if self.server_socket:
#             selected_index = self.file_listbox.curselection()
#             if selected_index:
#                 selected_filename = self.file_listbox.get(selected_index)
#                 self.server_socket.send(selected_filename.encode("utf-8"))
#                 filename = self.filename_entry.get()
#                 file = open(filename, 'wb')
#                 file_data = self.server_socket.recv(1024)
#                 while file_data:
#                     file.write(file_data)
#                     file_data = self.server_socket.recv(1024)
#                 file.close()
#                 self.status_label.config(text="File received successfully.")
#             else:
#                 self.status_label.config(text="Please select a file from the list.")
#         else:
#             self.status_label.config(text="Not connected to the server.")

# if __name__ == "__main__":
#     root = tk.Tk()
#     client_ui = ClientUI(root)
#     root.mainloop()

import tkinter as tk
import socket
from tkinter import filedialog

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

        self.file_listbox = tk.Listbox(master)
        self.file_listbox.pack()

        self.refresh_button = tk.Button(master, text="Refresh", command=self.refresh_file_list)
        self.refresh_button.pack()

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
            self.request_file_list()
        except Exception as e:
            self.status_label.config(text=f"Connection failed: {str(e)}")

    def request_file_list(self):
        self.server_socket.send(b"LIST_FILES")
        file_list = self.server_socket.recv(1024).decode("utf-8")
        files = file_list.split(",")
        self.file_listbox.delete(0, tk.END)
        for file in files:
            self.file_listbox.insert(tk.END, file)

    def refresh_file_list(self):
        if self.server_socket:
            self.request_file_list()
        else:
            self.status_label.config(text="Not connected to the server.")

    def receive_file(self):
        if self.server_socket:
            selected_index = self.file_listbox.curselection()
            if selected_index:
                try:
                    selected_filename = self.file_listbox.get(selected_index)
                    self.server_socket.send(selected_filename.encode("utf-8"))
                    filename = self.filename_entry.get()  # Get the filename from the entry
                    with open(filename, 'wb') as file:
                        while True:
                            file_data = self.server_socket.recv(1024)
                            if not file_data:
                                break
                            file.write(file_data)
                    self.status_label.config(text="File received successfully.")
                except Exception as e:
                    self.status_label.config(text=f"Error during file transfer: {str(e)}")
            else:
                self.status_label.config(text="Please select a file from the list.")
        else:
            self.status_label.config(text="Not connected to the server.")


if __name__ == "__main__":
    root = tk.Tk()
    client_ui = ClientUI(root)
    root.mainloop()
