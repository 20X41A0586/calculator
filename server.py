import socket
SERVER_HOST='127.0.0.1'
SERVER_PORT=12345
server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_socket.bind((SERVER_HOST,SERVER_PORT))
server_socket.listen(5)
print(f" server listing on {SERVER_HOST}:{SERVER_PORT}")
while True:
    client_socket,client_address=server_socket.accept()
    print(f"connection received from{client_address}")
    message=client_socket.recv(1024).decode()
    print(f"Message from client: {message}")
    
    client_socket.send("Hello from sevrer!".encode())
    client_socket.close()