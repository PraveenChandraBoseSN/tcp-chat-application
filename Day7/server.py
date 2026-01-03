import socket
import threading
def handle_client(cl_sck, cl_add):
    print(f"Client at address: {cl_add}")
    buffer = ""
    list_of_movies = ["Anabelle", "Conjuring", "Talk to Me", "LightsOut"]
    try:
        while True:
            raw_data = cl_sck.recv(1024)
            if not raw_data:
                break
            buffer += raw_data.decode()
            while "\n" in buffer:
                request, buffer = buffer.split("\n", 1)
                request = request.rstrip("\r").upper()
                if request == "EXIT":
                    cl_sck.send("BYE\n".encode())
                    return
                elif request == "LIST":
                    cl_sck.send(f"Here is the list of all available movies: {', '.join(list_of_movies)}\n".encode())
                elif request == "COUNT":
                    cl_sck.send(f"There are totally {len(list_of_movies)} movies in the list.\n".encode())
                elif request == "HELP":
                    cl_sck.send("Available commands:\n"
                                "LIST\n"
                                "COUNT\n"
                                "HELP\n"
                                "EXIT\n".encode())
                else:
                    cl_sck.send("ERROR: Unknown Command\n".encode())
    finally:
        cl_sck.close()
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
ip = "0.0.0.0"
port = 5000
add = (ip, port)
server_socket.bind(add)
server_socket.listen()
print("[SERVER STARTED LISTENING....]")
while True:
    client_socket, client_address = server_socket.accept()
    thread = threading.Thread(target=handle_client, args = (client_socket, client_address))
    thread.start()