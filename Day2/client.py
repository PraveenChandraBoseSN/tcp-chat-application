import socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip = "127.0.0.1"
prt = 5000
add = (ip, prt)
client.connect(add)
client.send("Hello Server!".encode())
client.close()