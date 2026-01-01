import socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip = "127.0.0.1"
port = 5000
add = (ip, port)
client_socket.connect(add)
commands = ["COUNT", "LIST", "HELP", "EXIT"]
try:
    while True:
        check = 0
        for i in commands:
            client_socket.send(i.encode())
            response = client_socket.recv(1024).decode()
            print(f"RESPONSE RECEIVED: \n{response}")
            if i == "EXIT":
                check+=1
                break
        if check:
            break
finally:
    client_socket.close()