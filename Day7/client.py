import socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip = "127.0.0.1"
port = 5000
add = (ip, port)
client_socket.connect(add)
commands = ["LIST\n", "COUNT\n", "HELP\n", "EXIT\n"]
for cmd in commands:
    client_socket.send(cmd.encode())

buffer = ""
try:
    while True:
        raw_data = client_socket.recv(1024)
        if not raw_data:
            break
        buffer += raw_data.decode()
        while "\n" in buffer:
            response, buffer = buffer.split("\n" ,1)
            print(f"Received Response: {response}")
finally:
    client_socket.close()