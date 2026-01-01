import socket
import threading
def handle_client(sc, ad):
    list_of_movies = ["Conjuring", "Anabelle", "Sinister", "LightsOut"]
    print(f"[CLIENT connected at]: {ad}")
    try:
        while True:
            raw_data = sc.recv(1024)
            if not raw_data:
                print("Nothing Received")
                break
            request = raw_data.decode().strip().upper()
            if request == "EXIT":
                sc.send("BYE".encode())
                break
            elif request == "COUNT":
                sc.send(f"There are totally {len(list_of_movies)} movies".encode())
            elif request == "LIST":
                sc.send(f"Available movies : {', '.join(list_of_movies)}".encode())
            elif request == "HELP":
                sc.send(f"Available commands:\n"
                        "LIST\n"
                        "COUNT\n"
                        "HELP\n"
                        "EXIT".encode())
            else:
                sc.send("ERROR: Unknown command".encode())
    finally:
        sc.close()
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
ip = "0.0.0.0"
port = 5000
add = (ip, port)
server_socket.bind(add)
server_socket.listen()
print("[SERVER Started Listening]....")
while True:
    client_socket, client_address = server_socket.accept()
    thread = threading.Thread(target=handle_client, args = (client_socket, client_address))
    thread.start()