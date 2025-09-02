import socket
s = socket.socket()
s.bind(('localhost', 8000))
s.listen(5)
print("Server started... Waiting for client...")
c, addr = s.accept()
print(f"Connected with {addr}")
while True:
    i = input("Enter data: ")         
    c.send(i.encode())             
    ack = c.recv(1024).decode()       
    if ack:
        print("Client says:", ack)
        continue
    else:
        c.close()
        break      