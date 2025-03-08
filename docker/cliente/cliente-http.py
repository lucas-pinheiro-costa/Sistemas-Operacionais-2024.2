import http.client
from concurrent.futures import ThreadPoolExecutor

def fazer_requisicao_get(id):
    print(f'### thread id {id} - Iniciou')
    # Conectar ao servidor localhost na porta 3000
    conexao = http.client.HTTPConnection("localhost", 3000)
    print(f'### thread id {id} - Abriu conexão')

    # Fazer a requisição GET
    conexao.request("GET", f"/{id}")
    print(f'### thread id {id} - Enviou requisição')

    # Obter a resposta
    resposta = conexao.getresponse()

    # Ler o conteúdo da resposta
    # conteudo = resposta.read()

    # Imprimir o status e o conteúdo da resposta
    print(f"Status ({id}): {resposta.status}")
    print(f"Motivo ({id}): {resposta.reason}")
    # print("Conteúdo:")
    # print(conteudo.decode("utf-8"))

    # Fechar a conexão
    conexao.close()
    print(f'### thread id {id} - Terminou')

# Chamar a função para fazer a requisição GET
# fazer_requisicao_get()

# Usar ThreadPoolExecutor para gerenciar threads
# with ThreadPoolExecutor(max_workers=2) as executor:
#     futuro1 = executor.submit(fazer_requisicao_get, 1)
#     futuro2 = executor.submit(fazer_requisicao_get, 2)

#     futuro1.result()
#     futuro2.result()

futuro = [0] * 10
with ThreadPoolExecutor(max_workers=10) as executor:
    for thread_id in range(10):
        futuro[thread_id] = executor.submit(fazer_requisicao_get, thread_id)

    for thread_id in range(10):
        futuro[thread_id].result()
