import random

# Gerar uma lista de 1000 números aleatórios
numeros = [random.randint(1, 100) for _ in range(1000)]

# Exportar a lista para um arquivo texto
with open('numeros_aleatorios.txt', 'w') as arquivo:
    for numero in numeros:
        arquivo.write(f"{numero}\n")

print("A lista de 1000 números aleatórios foi exportada para o arquivo 'numeros_aleatorios.txt'.")