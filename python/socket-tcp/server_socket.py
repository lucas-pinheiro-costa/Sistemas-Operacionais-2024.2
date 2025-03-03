import socketserver, socket, sys

class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        # self.request é o socket TCP conectado ao cliente
        self.data = self.request.recv(1024).strip()
        print("Recebido de {}:".format(self.client_address[0]))
        print(self.data)
        # apenas envia de volta os mesmos dados, mas em maiúsculas
        self.request.sendall(self.data.upper())

if __name__ == "__main__":
    HOST, PORT = "0.0.0.0", 8080  # Use "0.0.0.0" para escutar em todas as interfaces de rede

    # Criar o servidor, vinculando ao endereço e porta especificados
    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        print(f"Servidor rodando em {HOST}:{PORT}")
        # Ativar o servidor; isso manterá o servidor rodando até que
        # você interrompa o programa com Ctrl-C
        server.serve_forever()