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
                        "<!DOCTYPE html><html><head><title>Servidor Web | Unisinos</title>"
                        "<style>"
                        "body{margin:0;font-family:Arial,sans-serif;background:#f2f6fa;color:#17324d;}"
                        "header{background:#003b70;color:white;padding:20px 8%;"
                        "border-bottom:4px solid #58a6dc;}"
                        "header h1{margin:0;font-size:26px;}"
                        "header p{margin:6px 0 0;color:#d8ebf8;}"
                        "nav{margin-top:15px;}"
                        "nav a{color:white;text-decoration:none;margin-right:20px;font-weight:bold;}"
                        "main{max-width:1000px;margin:45px auto;padding:0 25px;}"
                        ".hero{background:white;padding:45px;border-radius:16px;"
                        "box-shadow:0 4px 15px rgba(0,0,0,.08);border-left:6px solid #58a6dc;}"
                        ".tag{color:#0066a1;font-weight:bold;font-size:13px;letter-spacing:1px;}"
                        "h2{font-size:38px;margin:12px 0;color:#003b70;}"
                        ".hero p{font-size:17px;line-height:1.7;color:#53697c;}"
                        ".cards{display:flex;gap:20px;margin-top:25px;}"
                        ".card{background:white;padding:25px;border-radius:14px;flex:1;"
                        "box-shadow:0 4px 15px rgba(0,0,0,.06);}"
                        ".card h3{color:#003b70;margin-top:0;}"
                        ".card p{line-height:1.6;color:#5b6f80;}"
                        ".status{margin-top:25px;background:#003b70;color:white;padding:22px;"
                        "border-radius:14px;}"
                        ".status strong{color:#8ed1f5;}"
                        ".button{display:inline-block;margin-top:18px;padding:12px 20px;"
                        "background:#0066a1;color:white;text-decoration:none;"
                        "border-radius:8px;font-weight:bold;}"
                        "footer{text-align:center;padding:25px;color:#708090;font-size:14px;}"
                        "@media(max-width:700px){.cards{flex-direction:column;}.hero{padding:30px;}"
                        "h2{font-size:30px;}}"
                        "</style></head>"
                        "<body>"
                        "<header>"
                        "<h1>Servidor Web</h1>"
                        "<p>Redes de Computadores • Unisinos</p>"
                        "<nav><a href=\"/\">Início</a><a href=\"/sobre\">Sobre</a></nav>"
                        "</header>"
                        "<main>"
                        "<section class=\"hero\">"
                        "<div class=\"tag\">TRABALHO PRÁTICO • SOCKETS TCP</div>"
                        "<h2>Servidor Web em Python</h2>"
                        "<p>Este servidor foi desenvolvido em Python utilizando sockets TCP. "
                        "Ele recebe requisições HTTP, identifica a rota solicitada e envia "
                        "uma resposta diretamente ao navegador.</p>"
                        "</section>"
                        "<section class=\"cards\">"
                        "<div class=\"card\"><h3>Socket</h3>"
                        "<p>Interface utilizada para permitir a comunicação entre aplicações "
                        "através da rede.</p></div>"
                        "<div class=\"card\"><h3>TCP</h3>"
                        "<p>Protocolo de transporte utilizado para estabelecer uma conexão "
                        "confiável entre cliente e servidor.</p></div>"
                        "<div class=\"card\"><h3>HTTP</h3>"
                        "<p>Protocolo utilizado pelo navegador para realizar requisições "
                        "e receber respostas do servidor.</p></div>"
                        "</section>"
                        "<div class=\"status\">"
                        "<strong>● SERVIDOR ATIVO</strong><br>"
                        "Socket TCP escutando na porta 8080."
                        "<br><a class=\"button\" href=\"/sobre\">Conheça o servidor →</a>"
                        "</div>"
                        "</main>"
                        "<footer>Ciência da Computação • Unisinos • Trabalho Prático de Redes</footer>"
                        "</body></html>"
                    )
                elif route == "/sobre":
                    response = (
                        "HTTP/1.1 200 OK\r\n"
                        "Content-Type: text/html; charset=utf-8\r\n\r\n"
                        "<!DOCTYPE html><html><head><title>Sobre | Servidor Web</title>"
                        "<style>"
                        "body{margin:0;font-family:Arial,sans-serif;background:#f2f6fa;color:#17324d;}"
                        "header{background:#003b70;color:white;padding:20px 8%;"
                        "border-bottom:4px solid #58a6dc;}"
                        "header h1{margin:0;font-size:26px;}"
                        "header p{margin:6px 0 0;color:#d8ebf8;}"
                        "nav{margin-top:15px;}"
                        "nav a{color:white;text-decoration:none;margin-right:20px;font-weight:bold;}"
                        "main{max-width:1000px;margin:45px auto;padding:0 25px;}"
                        ".intro{margin-bottom:25px;}"
                        ".tag{color:#0066a1;font-weight:bold;font-size:13px;letter-spacing:1px;}"
                        "h2{font-size:36px;margin:10px 0;color:#003b70;}"
                        ".intro p{font-size:17px;line-height:1.7;color:#53697c;}"
                        ".cards{display:flex;gap:20px;}"
                        ".card{background:white;padding:25px;border-radius:14px;flex:1;"
                        "box-shadow:0 4px 15px rgba(0,0,0,.06);}"
                        ".number{font-size:13px;color:#58a6dc;font-weight:bold;}"
                        ".card h3{color:#003b70;margin:10px 0;}"
                        ".card p{line-height:1.6;color:#5b6f80;}"
                        ".flow{margin-top:25px;background:#003b70;color:white;padding:25px;"
                        "border-radius:14px;}"
                        ".flow h3{margin-top:0;color:#8ed1f5;}"
                        ".flow p{line-height:1.7;}"
                        ".button{display:inline-block;margin-top:20px;padding:12px 20px;"
                        "background:#0066a1;color:white;text-decoration:none;"
                        "border-radius:8px;font-weight:bold;}"
                        "footer{text-align:center;padding:25px;color:#708090;font-size:14px;}"
                        "@media(max-width:700px){.cards{flex-direction:column;}}"
                        "</style></head>"
                        "<body>"
                        "<header>"
                        "<h1>Servidor Web</h1>"
                        "<p>Redes de Computadores • Unisinos</p>"
                        "<nav><a href=\"/\">Início</a><a href=\"/sobre\">Sobre</a></nav>"
                        "</header>"
                        "<main>"
                        "<section class=\"intro\">"
                        "<div class=\"tag\">COMO FUNCIONA</div>"
                        "<h2>Sobre o servidor</h2>"
                        "<p>Este trabalho demonstra, de forma prática, como um servidor Web "
                        "pode ser construído utilizando diretamente sockets TCP em Python.</p>"
                        "</section>"
                        "<section class=\"cards\">"
                        "<div class=\"card\">"
                        "<div class=\"number\">01 — SOCKET</div>"
                        "<h3>Socket</h3>"
                        "<p>É a interface utilizada pelo programa para estabelecer a "
                        "comunicação entre o cliente e o servidor.</p>"
                        "</div>"
                        "<div class=\"card\">"
                        "<div class=\"number\">02 — TCP</div>"
                        "<h3>TCP</h3>"
                        "<p>O TCP estabelece uma conexão entre as aplicações e garante que "
                        "os dados sejam entregues de maneira ordenada.</p>"
                        "</div>"
                        "<div class=\"card\">"
                        "<div class=\"number\">03 — HTTP</div>"
                        "<h3>HTTP</h3>"
                        "<p>O navegador utiliza HTTP para enviar a requisição e receber "
                        "a resposta produzida pelo servidor.</p>"
                        "</div>"
                        "</section>"
                        "<section class=\"flow\">"
                        "<h3>Fluxo da comunicação</h3>"
                        "<p>Navegador → conexão TCP → servidor → requisição HTTP → "
                        "processamento da rota → resposta HTTP → navegador.</p>"
                        "<a class=\"button\" href=\"/\">← Voltar para o início</a>"
                        "</section>"
                        "</main>"
                        "<footer>Ciência da Computação • Unisinos • Trabalho Prático de Redes</footer>"
                        "</body></html>"
                    )
                else:
                    response = (
                        "HTTP/1.1 404 Not Found\r\n"
                        "Content-Type: text/html; charset=utf-8\r\n\r\n"
                        "<!DOCTYPE html><html><head><title>404 | Página não encontrada</title>"
                        "<style>"
                        "body{margin:0;font-family:Arial,sans-serif;background:#f2f6fa;"
                        "color:#17324d;display:flex;align-items:center;justify-content:center;"
                        "min-height:100vh;text-align:center;}"
                        ".card{background:white;padding:50px;max-width:550px;margin:20px;"
                        "border-radius:18px;box-shadow:0 4px 20px rgba(0,0,0,.08);}"
                        "h1{font-size:70px;margin:0;color:#003b70;}"
                        "h2{color:#17324d;margin:5px 0 15px;}"
                        "p{color:#637789;line-height:1.6;}"
                        "a{display:inline-block;margin-top:15px;padding:12px 22px;"
                        "background:#0066a1;color:white;text-decoration:none;"
                        "border-radius:8px;font-weight:bold;}"
                        "</style></head>"
                        "<body>"
                        "<div class=\"card\">"
                        "<h1>404</h1>"
                        "<h2>Página não encontrada</h2>"
                        "<p>O recurso solicitado não existe neste servidor.</p>"
                        "<a href=\"/\">Voltar para o início</a>"
                        "</div>"
                        "</body></html>"
                    )
                # 8: send HTTP response and close client socket
                client_socket.sendall(response.encode('utf-8'))
        client_socket.close()

if __name__ == "__main__":
    start_server()
