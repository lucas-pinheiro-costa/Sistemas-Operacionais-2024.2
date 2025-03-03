import socketserver, socket, sys

# hostname = socket.gethostname()
# local_ip = socket.gethostbyname(hostname)

class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    A classe manipuladora de requisições para nosso servidor.

    Ela é instanciada uma vez por conexão ao servidor e deve
    sobrescrever o método handle() para implementar a comunicação
    com o cliente.
    """

    def handle(self):
        # self.request é o socket TCP conectado ao cliente
        self.data = self.request.recv(1024).strip()
        print("Recebido de {}:".format(self.client_address[0]))
        print(self.data)
        # apenas envia de volta os mesmos dados, mas em maiúsculas
        self.request.sendall(self.data.upper())

if __name__ == "__main__":
    HOST, PORT = "10.25.2.25", 80
    data = " ".join(sys.argv[1:])

    # Criar um socket (SOCK_STREAM significa um socket TCP)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        # Conectar ao servidor e enviar dados
        sock.connect((HOST, PORT))
        sock.sendall(bytes(data + "\n", "utf-8"))

        # Receber dados do servidor e encerrar
        received = str(sock.recv(1024), "utf-8")

    print("Sent:     {}".format(data))
    print("Received: {}".format(received))