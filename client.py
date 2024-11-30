import socket
SERVER_HOST='127.0.01'
SERVER_PORT=12345
client_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
try:
    client_socket.connect((SERVER_HOST,SERVER_PORT))
    print(f"connected to the sevrer at {SERVER_HOST}:{SERVER_PORT}")
    
    client_socket.send("Hello eberu one".encode())
    
    response=client_socket.recv(1024).decode()
    print(f"message from server: {response}")
finally:
    client_socket.close()
    