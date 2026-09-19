import socket

PORT = 8080
BUFFER_SIZE = 2048

# af_inet: USE IPV4
# sock_stream = TCP

def start_server():
    # 1: create TCP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 2: configure port reuse
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # 3: bind the socket to the address and port
    # ('' means will listen in all network interfaces)
    server_socket.bind(('', PORT))
    # 4: put socket into listen mode. will limit the queue of pending conections to 10
    server_socket.listen(10)

    print(f"Server running on port {PORT}...")
    print(f"Access http://localhost:{PORT}/ in your browser")

    # 5: main event loop
    while True:
        # () accept blocks execution until an incoming client connection arrives
        # returns a tuple cointaining:
        # client_socket is the new socket to communicate with this client
        # addr: tupple containing IP_client and port_client
        client_socket, addr = server_socket.accept()
        print(f"Connection acepted from {addr}")

        # 6: receive and decode the HTTP request
        request_bytes = client_socket.recv(BUFFER_SIZE)
        request_text  = request_bytes.decode('utf-8', errors='ignore')

        if not request_text:
            client_socket.close()
            continue

        print("RECEIVED REQUEST!")
        print(request_text)
        print("\n")

        #7: route parsing and HTTP response construction
        lines = request_text.split('\n')
        first_line = lines[0].split()

        # ensure the request line contains at least the HTPP method and path
        if len(first_line) >= 2:
            method = first_line[0]
            route = first_line[1]

            if method == "GET":
                if route == "/":
                    response = (
                        "HTTP/1.1 200 OK\r\n"
                        "Content-Type: text/html; charset=utf-8\r\n\r\n"
                        "<!DOCTYPE html><html><head><title>Home</title></head>"
                        "<body><h1>Página Principal</h1>"
                        "<p>Bem-vindo ao servidor Web implementado em Python com Sockets TCP!</p>"
                        "</body></html>"
                    )
                else:
                    response = (
                        "HTTP/1.1 404 Not Found\r\n"
                        "Content-Type: text/html; charset=utf-8\r\n\r\n"
                        "<!DOCTYPE html><html><head><title>404 Not Found</title></head>"
                        "<body><h1>404 Not Found</h1>"
                        "<p>O recurso solicitado não existe neste servidor.</p>"
                        "</body></html>"
                    )
                # 8: send HTTP response and close client socket
                client_socket.sendall(response.encode('utf-8'))
        client_socket.close()

if __name__ == "__main__":
    start_server()




