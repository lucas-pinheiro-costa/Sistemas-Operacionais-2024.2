import threading
import os
import sys

def soma_numeros(numeros, resultado, indice):
    resultado[indice] = sum(numeros)

def main():
    # Acesso ao arquivo de números aleatórios
    nome_arquivo = 'numeros_aleatorios.txt'
    
    # Verifica se o arquivo existe
    if not os.path.exists(nome_arquivo):
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")
        print("Por favor, execute 'randomNumberGenerator.py' primeiro para gerar o arquivo.")
        sys.exit(1)

    # Função para ler números do arquivo
    def ler_numeros_do_arquivo(nome_arquivo):
        with open(nome_arquivo, 'r') as arquivo:
            numeros = [int(linha.strip()) for linha in arquivo]
            # o método strip() ajuda a remover quaisquer caracteres de espaço em branco no início ou no fim
        return numeros

    # Chama a função para transferir números para uma lista
    numeros = ler_numeros_do_arquivo(nome_arquivo)

    # Divide a lista em 10 partes
    tamanho = len(numeros) // 10
    partes = [numeros[i * tamanho:(i + 1) * tamanho] for i in range(10)]
    # aqui uma lista chamada 'partes' possui 10 listas dentro dela.
    resultados = [0] * 10
    # já a lista 'resultados' possui 10 elementos, cada um com valor 0.

    # Cria e inicia 10 threads, cada uma com uma parte da lista de números
    threads = []
    for i in range(10):
        thread = threading.Thread(target=soma_numeros, args=(partes[i], resultados, i))
        threads.append(thread)
        thread.start()

    # Aguarda todas as threads terminarem
    for thread in threads:
        thread.join()

    # Soma o resultado final e imprime
    soma_total = sum(resultados)
    print(f"Soma total: {soma_total}")

if __name__ == "__main__":
    main()