import http.client
import threading

# Função para fazer uma requisição GET
def fazer_requisicao_get():
    try:
        # Conectar ao servidor localhost na porta 8000
        conexao = http.client.HTTPConnection("localhost", 8000)

        # Fazer a requisição GET
        conexao.request("GET", "/")

        # Obter a resposta
        resposta = conexao.getresponse()

        # Ler o conteúdo da resposta
        conteudo = resposta.read()

        # Imprimir o status e o conteúdo da resposta
        print(f"Status: {resposta.status}")
        print(f"Motivo: {resposta.reason}")
        print("Conteúdo:")
        print(conteudo.decode("utf-8"))

        # Fechar a conexão
        conexao.close()
    except Exception as e:
        print(f"Erro na requisição: {e}")

# Função para criar e iniciar threads
def executar_clientes_simultaneos(num_clientes):
    threads = []
    for i in range(num_clientes):
        # Criar uma thread para cada cliente
        thread = threading.Thread(target=fazer_requisicao_get)
        threads.append(thread)
        thread.start()

    # Aguardar todas as threads terminarem
    for thread in threads:
        thread.join()

# Executar clientes simultâneos
if __name__ == "__main__":
    num_clientes = 2  # Altere este valor para 1, 2, 5 ou 10
    print(f"Iniciando {num_clientes} clientes simultâneos...")
    executar_clientes_simultaneos(num_clientes)
    print("Todos os clientes terminaram.")