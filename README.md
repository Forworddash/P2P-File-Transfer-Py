# P2P-File-Transfer-Py
The Python project is a P2P (peer-to-peer) file transfer system comprising two main components: a server and a client. The project utilizes Python and the Tkinter library for creating a simple graphical user interface (GUI) for the client.

Server:
The server is responsible for handling incoming connections from clients.
It binds to a specified host and port, listens for connections, and accepts them when clients connect.
The server allows clients to request files or receive a list of available files.

Client:
The client connects to the server using a provided hostname and port.
It features a GUI built with Tkinter, allowing users to connect to the server, view a list of available files, and receive selected files from the server.
Users can also refresh the file list to get updated information from the server.

File Transfer:
The file transfer process involves selecting a file from the server's list and specifying a local filename for the received file.
The server sends the selected file's content to the client for storage in the specified local file.

Technology Used:
Programming Language: Python
GUI Library: Tkinter (for the client UI)
Networking: Socket programming is used for communication between the server and clients.
File Handling: Basic file operations (open, read, write) are employed for file transfer.
The project enables users to establish a connection, view available files on the server, and receive selected files through a simple and intuitive graphical interface. The P2P file transfer system is built using core Python features, making it platform-independent and easily deployable on various systems.




# How to setup
1. Run server_ui.py first in terminal while in root directory 'python server_ui.py' *make sure python is installed on your system
2. Run client_ui.py on a second terminal using 'python client_ui.py'
3. Copy the hostname from server.py and paste in client.py (default: 127.0.0.1)
4. In your client, select the file you wish to download > enter a name to save it > receive file

