import socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip = socket.gethostbyname(socket.gethostname())
port = 5000
addr = (ip, port)
server_socket.bind(addr)
server_socket.listen(1)
print("[SERVER STARTED LISTENING...]")
client_sck, client_addr = server_socket.accept()
print(f"Client Address: {client_addr}")
server_socket.close()