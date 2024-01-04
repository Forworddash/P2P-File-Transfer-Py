import tkinter as tk
from server import Server

class ServerUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Server")

        self.label = tk.Label(self.root, text="Server is running.")
        self.label.pack()

        self.quit_button = tk.Button(self.root, text="Quit", command=self.root.quit)
        self.quit_button.pack()

        self.server = Server("127.0.0.1", 8080)

    def start(self):
        self.server.start()
        self.root.mainloop()

if __name__ == "__main__":
    server_ui = ServerUI()
    server_ui.start()
