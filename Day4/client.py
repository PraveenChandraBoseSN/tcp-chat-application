import socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip = "127.0.0.1"
port = 5000
add = (ip, port)
client_socket.connect(add)
client_socket.send("LIST".encode())
data = client_socket.recv(1024).decode()
print(f"Response Received: {data}")
client_socket.close()