import socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
ip = "0.0.0.0"
prt = 5000
add = (ip, prt)
server.bind(add)
server.listen(1)
print("[SERVER STARTED LISTENING....]")
cl_sck, cl_add = server.accept()
data = cl_sck.recv(1024)
print(f"Message from the client: {data.decode()}")