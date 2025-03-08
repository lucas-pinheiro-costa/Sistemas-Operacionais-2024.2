import http.client
from multiprocessing import Process

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

# Função para criar e iniciar processos
def executar_clientes_simultaneos(num_clientes):
    processos = []
    for i in range(num_clientes):
        processo = Process(target=fazer_requisicao_get)
        processos.append(processo)
        processo.start()

    # Aguardar todos os processos terminarem
    for processo in processos:
        processo.join()

# Executar clientes simultâneos
if __name__ == "__main__":
    num_clientes = 5  # Altere este valor para 1, 2, 5 ou 10
    executar_clientes_simultaneos(num_clientes)