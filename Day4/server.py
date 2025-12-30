import socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
ip = '0.0.0.0'
port = 5000
add = (ip, port)
server_socket.bind(add)
server_socket.listen(1)
print("[SERVER IS LISTENING]....")
client_socket, client_address = server_socket.accept()
print(f"[CLIENT AT]: {client_address}")
data = client_socket.recv(1024).decode().strip()
print(f"[CLIENT HAS ASKED FOR]: {data}")
list_of_movies = ["Conjuring", "LightsOut", "Anabelle", "Dominick"]
if "COUNT" == data.upper():
    client_socket.send(f"Total count of movies: {len(list_of_movies)}".encode())
elif "LIST" == data.upper():
    client_socket.send("\n".join(list_of_movies).encode())
elif "HELP" == data.upper():
    client_socket.send("Available commands\n"
                       "COUNT\n"
                       "LIST\n"
                       "HELP\n".encode())
else:
    client_socket.send("ERROR: Unknown Command".encode())
client_socket.close()
server_socket.close()