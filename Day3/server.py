import socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
ip = "0.0.0.0"
port = 5000
add = (ip, port)
server.bind(add)
server.listen(1)
print("[SERVER IS LISTENING]....")
client_socket, client_address = server.accept()
print(f"Address of the client: {client_address}")
request = client_socket.recv(1024)
print(f"Request from the client: {request.decode()}")
client_socket.send("Here are the list of the movies:\n" 
                    "* Conjuring\n"
                    "* Anabelle\n"
                    "* Baghead\n"
                    "* Lights Out\n".encode())
client_socket.close()
server.close()