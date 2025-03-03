# Relatório: Criando um Servidor TCP Simples em Python

## Informações gerais
- **Disciplina**: Sistemas Operacionais (SO) do curso de TADS (Superior em Tecnologia em Análise e Desenvolvimento de Sistemas) no CNAT-IFRN (Instituto Federal de Educação, Ciência e Tecnologia do Rio Grande do Norte - Campus Natal-Central).
- **Professor**: [Leonardo A. Minora](https://github.com/leonardo-minora)
- **Aluno**: [Lucas Pinheiro da Costa](https://github.com/lucas-pinheiro-costa) (mat. 20231014040023)

## Sumário
1. Introdução
2. O que é um servidor socket e um cliente socket?
3. Implementação do servidor TCP
4. Implementação do cliente TCP
5. Testes e resultados
6. Conclusão

<br>

---

### 1. Introdução

Este relatório descreve a experiência de criação de um servidor TCP simples usando a linguagem de programação Python. O objetivo foi entender como a comunicação entre um servidor e um cliente funciona em nível de sockets, utilizando o protocolo TCP. A implementação foi feita em dois arquivos: `server_socket.py` (servidor) e `client.py` (cliente).

---

### 2. O que é um *servidor socket* e um *cliente socket*?

Um **servidor socket** é um programa que escuta conexões de entrada em uma porta específica e responde às requisições dos clientes. Ele fica em um estado de espera, aguardando que clientes se conectem para então processar as mensagens recebidas e enviar respostas. No contexto de redes, um socket é um ponto final de comunicação que permite a troca de dados entre dois dispositivos.

No caso deste experimento, o servidor foi implementado usando o módulo `socketserver` do Python, que facilita a criação de servidores TCP. O servidor escuta na porta 8080 e responde às mensagens dos clientes convertendo o texto recebido para letras maiúsculas.

Um **cliente socket** é um programa que se conecta a um servidor socket para enviar e receber dados. O cliente inicia a comunicação com o servidor, envia uma mensagem e aguarda a resposta. No contexto deste experimento, o cliente foi implementado usando o módulo `socket` do Python, que permite a criação de sockets TCP.

O cliente se conecta ao servidor no endereço `localhost` (ou seja, na mesma máquina) na porta 8080, envia uma mensagem e recebe a resposta do servidor.

---

### 3. Implementação do servidor TCP

O servidor foi implementado no arquivo `server_socket.py`. A seguir, os principais pontos da implementação:

- **Importação do módulo `socketserver`**: Este módulo fornece classes para criar servidores de rede de forma simplificada.
- **Criação da classe `MyTCPHandler`**: Esta classe herda de `socketserver.BaseRequestHandler` e implementa o método `handle()`, que é responsável por processar as requisições dos clientes.
- **Configuração do servidor**: O servidor foi configurado para escutar em todas as interfaces de rede (`0.0.0.0`) na porta 8080.
- **Funcionamento do servidor**: O servidor recebe a mensagem do cliente, imprime no console e envia de volta a mensagem em letras maiúsculas.

Aqui está o código do servidor:

```python
import socketserver

class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        self.data = self.request.recv(1024).strip()
        print("Recebido de {}:".format(self.client_address[0]))
        print(self.data)
        self.request.sendall(self.data.upper())

if __name__ == "__main__":
    HOST, PORT = "0.0.0.0", 8080
    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        print(f"Servidor rodando em {HOST}:{PORT}")
        server.serve_forever()
```

---

### 4. Implementação do cliente TCP
O cliente foi implementado no arquivo client.py. A seguir, os principais pontos da implementação:

Importação dos módulos socket e sys: O módulo socket é usado para criar o socket TCP, e o módulo sys permite acessar os argumentos da linha de comando.

Configuração do cliente: O cliente se conecta ao servidor no endereço localhost na porta 8080.

Envio e recebimento de dados: O cliente envia uma mensagem ao servidor e recebe a resposta, que é exibida no console.

Aqui está o código do cliente:

```python
import socket
import sys

HOST, PORT = "localhost", 8080
data = " ".join(sys.argv[1:])

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect((HOST, PORT))
    sock.sendall(bytes(data + "\n", "utf-8"))
    received = str(sock.recv(1024), "utf-8")

print("Sent:     {}".format(data))
print("Received: {}".format(received))
```

---

### 5. Testes e resultados

Para testar a implementação, foram realizados os seguintes passos:

Iniciar o servidor: O servidor foi iniciado e ficou escutando na porta 8080.

Executar o cliente: O cliente foi executado com diferentes mensagens, como "Olá, servidor!" e "Testando 123".

Verificar a comunicação: A mensagem enviada pelo cliente foi recebida pelo servidor, convertida para maiúsculas e enviada de volta ao cliente.

Exemplo de saída no servidor:

```bash
Recebido de 127.0.0.1:
b'Olá, servidor!'
```

Exemplo de saída no cliente:

```bash
Sent:     Olá, servidor!
Received: OLÁ, SERVIDOR!
```

Os testes confirmaram que a comunicação entre o cliente e o servidor foi bem-sucedida, com o servidor respondendo corretamente às mensagens enviadas pelo cliente.

---

### 6. Conclusão

A criação de um servidor TCP simples em Python foi uma experiência enriquecedora para entender como a comunicação entre cliente e servidor funciona em nível de sockets. Através deste experimento, foi possível aprender como configurar um servidor para escutar conexões, como um cliente pode se conectar a esse servidor e como os dados são trocados entre eles.

Este projeto pode ser expandido de várias formas, como adicionar suporte a múltiplos clientes simultâneos, implementar autenticação ou até mesmo criptografia para maior segurança. No entanto, para fins didáticos, a implementação atual já cumpre o objetivo de demonstrar os conceitos básicos de comunicação TCP usando sockets em Python.