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
5. Considerações finais

<br>

---

### 1. Introdução

Este relatório descreve a experiência de criação de um servidor HTTP simples usando a linguagem de programação Python. O objetivo foi entender como um servidor HTTP pode ser implementado e como ele lida com requisições de múltiplos clientes, tanto sem o uso de threads quanto com o uso de threads. A implementação foi feita em dois arquivos principais: `servidor_http.py` (servidor) e `cliente_http.py` (cliente). O servidor foi testado com diferentes números de clientes simultâneos (1, 2, 5 e 10) para observar o comportamento em ambos os cenários (com e sem threads).

---

### 2. Experimento 01: testando o servidor HTTP, **sem threads**, para 1, 2, 5 e 10 clientes simultâneos

#### Objetivo
O objetivo deste experimento foi testar o servidor HTTP sem o uso de threads, observando como ele lida com requisições de 1, 2, 5 e 10 clientes simultâneos.

#### Metodologia
1. **Servidor HTTP sem threads**:
   - O servidor foi implementado usando o módulo `http.server` do Python, sem a utilização de threads. Isso significa que o servidor processa uma requisição por vez, de forma sequencial.
   - O código do servidor foi configurado para rodar na porta `8000` e responder a requisições GET com um conteúdo HTML fixo.

![Resposta do Servidor sem Threads](imagens/http_semThreads_5Clientes_terminalServidor.jpg)

2. **Cliente HTTP**:
   - O cliente foi implementado usando o módulo `http.client` do Python.
   - Para simular clientes simultâneos, foi utilizado o módulo `multiprocessing`, que permite criar processos independentes para cada cliente.

![Resposta do Cliente sem Threads](imagens/http_semThreads_5Clientes.jpg)

3. **Testes**:
   - O servidor foi testado com 1, 2, 5 e 10 clientes simultâneos. Para cada teste, o tempo de resposta e o comportamento do servidor foram observados.

#### Resultados
- **1 Cliente**:
  - O servidor processou a requisição rapidamente, sem atrasos perceptíveis.
  - O tempo de resposta foi mínimo, já que não havia outras requisições em espera.

- **2 Clientes**:
  - O servidor processou as requisições sequencialmente. Enquanto uma requisição era processada, a outra ficava em espera.
  - O tempo total de resposta foi maior, pois o servidor não consegue paralelizar o processamento.

- **5 Clientes**:
  - O servidor continuou processando as requisições uma por uma, resultando em um tempo de resposta ainda maior.
  - As requisições adicionais ficaram em espera até que as anteriores fossem concluídas.

- **10 Clientes**:
  - O servidor mostrou um atraso significativo no tempo de resposta, já que todas as requisições foram processadas sequencialmente.
  - O tempo total para processar todas as requisições foi consideravelmente maior.

#### Conclusão
O servidor HTTP sem threads é capaz de lidar com requisições de forma sequencial, o que é adequado para um número pequeno de clientes. No entanto, à medida que o número de clientes aumenta, o tempo de resposta também aumenta significativamente, pois o servidor não consegue processar múltiplas requisições simultaneamente.

---

### 3. Experimento 02: testando o servidor HTTP, **com threads**, para 1, 2, 5 e 10 clientes simultâneos

#### Objetivo
O objetivo deste experimento foi testar o servidor HTTP com o uso de threads, observando como ele lida com requisições de 1, 2, 5 e 10 clientes simultâneos.

#### Metodologia
1. **Servidor HTTP com threads**:
   - O servidor foi modificado para utilizar threads, permitindo que ele processe múltiplas requisições simultaneamente.
   - Para isso, foi utilizado o módulo `socketserver` com `ThreadingMixIn`, que permite criar um servidor multithread.

2. **Cliente HTTP**:
   - O cliente foi implementado usando o módulo `http.client` do Python.
   - Para simular clientes simultâneos, foi utilizado o módulo `threading`, que permite criar threads independentes para cada cliente.

3. **Testes**:
   - O servidor foi testado com 1, 2, 5 e 10 clientes simultâneos. O tempo de resposta e o comportamento do servidor foram observados.

#### Resultados

- **1 Cliente**:
  - O servidor processou a requisição rapidamente, sem atrasos perceptíveis.
  - O tempo de resposta foi mínimo, semelhante ao Experimento 01.

- **2 Clientes**:
  - O servidor processou as requisições simultaneamente, sem atrasos significativos.
  - O tempo de resposta foi menor em comparação ao servidor sem threads.

- **5 Clientes**:
  - O servidor continuou processando as requisições simultaneamente, com um tempo de resposta consistente.
  - Não houve atrasos significativos, mesmo com um número maior de clientes.

- **10 Clientes**:
  - O servidor mostrou um desempenho estável, processando todas as requisições simultaneamente.
  - O tempo de resposta foi consideravelmente menor em comparação ao servidor sem threads.

- O uso de threads no cliente permitiu simular múltiplos clientes de forma eficiente, sem a necessidade de criar processos separados.
- O servidor processou todas as requisições simultaneamente, demonstrando a eficácia do uso de threads tanto no servidor quanto no cliente.

#### Conclusão
O servidor HTTP com threads é capaz de lidar com múltiplas requisições simultaneamente, resultando em um tempo de resposta menor e um desempenho mais estável, especialmente com um número maior de clientes. A utilização de threads permite que o servidor seja mais escalável e eficiente.

---

### 4. Diferenças entre ambos os experimentos

#### Desempenho
- **Servidor sem threads**:
  - Processa uma requisição por vez, resultando em um tempo de resposta maior à medida que o número de clientes aumenta.
  - Adequado para cenários com poucos clientes ou onde a simultaneidade não é crítica.

- **Servidor com threads**:
  - Processa múltiplas requisições simultaneamente, resultando em um tempo de resposta menor e um desempenho mais estável.
  - Adequado para cenários com um grande número de clientes ou onde a simultaneidade é essencial.

- **Uso de Threads no Cliente**:
  - No Experimento 02, o cliente utilizou threads para simular clientes simultâneos, o que é mais leve e eficiente em termos de recursos do sistema em comparação com o uso de processos (`multiprocessing`).
  - Threads compartilham memória, o que torna a simulação de clientes simultâneos mais simples, mas pode limitar o paralelismo em operações intensivas de CPU devido ao GIL (Global Interpreter Lock) do Python.

#### Escalabilidade
- **Servidor sem threads**:
  - Não é escalável para um grande número de clientes, pois o tempo de resposta aumenta significativamente com o aumento do número de requisições.

- **Servidor com threads**:
  - É escalável, podendo lidar com um grande número de clientes sem um aumento significativo no tempo de resposta.

#### Complexidade
- **Servidor sem threads**:
  - Mais simples de implementar, pois não requer o gerenciamento de threads.
  - Ideal para aplicações simples ou de baixa demanda.

- **Servidor com threads**:
  - Requer um gerenciamento mais cuidadoso de threads, o que pode aumentar a complexidade do código.
  - Ideal para aplicações que precisam lidar com múltiplas requisições simultaneamente.

#### Conclusão geral
A escolha entre um servidor HTTP com ou sem threads depende das necessidades da aplicação. Para cenários com poucos clientes ou baixa demanda, um servidor sem threads pode ser suficiente. No entanto, para cenários com um grande número de clientes ou alta demanda, um servidor com threads é a melhor opção, pois oferece um desempenho superior e maior escalabilidade.

---

### Considerações Finais

Este experimento permitiu compreender as diferenças entre um servidor HTTP sem threads e um servidor HTTP com threads. A utilização de threads melhora significativamente o desempenho e a escalabilidade do servidor, especialmente em cenários com múltiplos clientes simultâneos. No entanto, a implementação de um servidor com threads requer um gerenciamento mais cuidadoso e pode aumentar a complexidade do código. Portanto, a escolha entre as duas abordagens deve ser feita com base nas necessidades específicas da aplicação.
O uso de threads no cliente, em conjunto com o servidor multithread, demonstrou ser uma abordagem eficiente para simular múltiplos clientes simultâneos. Essa combinação permite um melhor aproveitamento dos recursos do sistema e um tempo de resposta mais rápido em cenários com alta demanda.