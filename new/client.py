import socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 12345
client_socket.connect((host, port))
client_socket.send("Hello from Client!".encode())
data = client_socket.recv(1024).decode()
print(f"Server says: {data}")
client_socket.close()