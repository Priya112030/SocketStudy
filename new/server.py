import socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'   
port = 12345
server_socket.bind((host, port))
server_socket.listen(1)
print(f"Server listening on {host}:{port}")
conn, addr = server_socket.accept()
print(f"Connected by {addr}")
data = conn.recv(1024).decode()
print(f"Client says: {data}")
conn.send("Hello from Server!".encode())
conn.close()
server_socket.close()