import socket
s = socket.socket()
s.connect(('localhost', 8000))

while True:
    data = s.recv(1024).decode()     
    print("Server says:", data)
    s.send("Acknowledgement Received".encode())