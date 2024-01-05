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

        self.filename_label = tk.Label(master, text="Enter filename for incoming file:")
        self.filename_label.pack()

        self.filename_entry = tk.Entry(master)
        self.filename_entry.pack()

        self.receive_button = tk.Button(master, text="Receive File", command=self.receive_file)
        self.receive_button.pack()

        self.quit_button = tk.Button(master, text="Quit", command=master.quit)
        self.quit_button.pack()

        self.server_socket = None

        # master.protocol("WM_DELETE_WINDOW", self.on_closing)

    def on_closing(self):
        if self.server_socket:
            self.server_socket.close()
        self.master.destroy()

    def connect_to_server(self):
        host = self.hostname_entry.get()
        port = 8080
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            self.server_socket.connect((host, port))
            self.status_label.config(text="Connected to the server.")
            # self.request_file_list()
        except Exception as e:
            self.status_label.config(text=f"Connection failed: {str(e)}")

    # def request_file_list(self):
    #     self.server_socket.send(b"LIST_FILES")
    #     file_list = self.server_socket.recv(1024).decode("utf-8")
    #     files = file_list.split(",")
    #     self.file_listbox.delete(0, tk.END)
    #     for file in files:
    #         self.file_listbox.insert(tk.END, file)

    def receive_file(self):
        print('receive_file start')
        if self.server_socket:
            selected_index = self.file_listbox.curselection()
            print(selected_index)
            if selected_index:
                try:
                    selected_filename = self.file_listbox.get(selected_index)
                    print('selected_filename: ', selected_filename)
                    self.server_socket.send(selected_filename.encode("utf-8"))
                    print('1')
                    filename = self.filename_entry.get()  # Get the filename from the entry
                    with open(filename, 'wb') as file:
                        while True:
                            # exception here
                            file_data = self.server_socket.recv(1024)
                            if not file_data:
                                break
                            file.write(file_data)
                    self.status_label.config(text="File received successfully.")
                except Exception as e:
                    print('8')
                    self.status_label.config(text=f"Error during file transfer: {str(e)}")
                # finally:
                #     self.server_socket.close()
            else:
                self.status_label.config(text="Please select a file from the list.")
        else:
            self.status_label.config(text="Not connected to the server.")
        print('receive_file end')
if __name__ == "__main__":
    root = tk.Tk()
    client_ui = ClientUI(root)
    root.mainloop()
