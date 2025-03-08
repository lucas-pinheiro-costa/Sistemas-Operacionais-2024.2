# Relatório: Criando um Servidor HTTP Simples em Python

## Informações gerais

- **Disciplina**: Sistemas Operacionais (SO) do curso de TADS (Superior em Tecnologia em Análise e Desenvolvimento de Sistemas) no CNAT-IFRN (Instituto Federal de Educação, Ciência e Tecnologia do Rio Grande do Norte - Campus Natal-Central).
- **Professor**: [Leonardo A. Minora](https://github.com/leonardo-minora)
- **Aluno**: [Lucas Pinheiro da Costa](https://github.com/lucas-pinheiro-costa) (mat. 20231014040023)

## Sumário

1. Introdução
2. Experimento 01: testando o servidor HTTP, **sem threads**, para 1, 2, 5 e 10 clientes simultâneos
3. Experimento 02: testando o servidor HTTP, **com threads**, para 1, 2, 5 e 10 clientes simultâneos
4. Diferenças entre ambos os experimentos


<br>

---

### 1. Introdução

Este relatório descreve a experiência de criação de um servidor TCP simples usando a linguagem de programação Python. O objetivo foi entender como a comunicação entre um servidor e um cliente funciona em nível de sockets, utilizando o protocolo TCP. A implementação foi feita em dois arquivos: `server_socket.py` (servidor) e `client.py` (cliente).

---

