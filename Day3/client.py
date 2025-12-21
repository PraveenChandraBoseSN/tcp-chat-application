import socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip = "127.0.0.1"
port = 5000
add = (ip, port)
client.connect(add)
client.send("I need a list of few horror movies".encode())
response = client.recv(1024)
print(f"Received Response: {response.decode()}")
client.close()