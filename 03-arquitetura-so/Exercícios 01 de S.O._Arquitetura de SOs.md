|   | INSTITUTO FEDERAL DO RN Campus Natal-Central |
| :---- | ----- |
|  | **Disciplina:** Sistemas Operacionais |
|  | **Professor(a):** Leonardo Ataide Minora |
|  | **Discente:** Lucas Pinheiro da Costa |
|	| **Matrícula:** 20231014040023 |
|  | **Curso:** TADS |
|	| **Semestre:** 2024.2 |
|  | **Resolução:** Lista de exercícios do Cap. 03 do livro “Sistemas Operacionais: Conceitos e Mecanismos” |


<br>
CAPÍTULO 03 - ARQUITETURAS DE SISTEMAS OPERACIONAIS
<br><br>

1. Monte uma tabela com os benefícios e deficiências mais relevantes das principais arquiteturas de sistemas operacionais.

| Arquitetura | Benefícios | Deficiências |
| :---- | :---- | :---- |
| **Sistemas Monolíticos** | • Alto desempenho devido à comunicação direta entre componentes. <br>• Menor tamanho do núcleo, com menos overhead. | • Alta complexidade e difícil manutenção. <br>• Um erro no núcleo pode comprometer todo o sistema. |
| **Sistemas Micronúcleo** | • Estabilidade elevada, pois suas funções são isoladas. <br>• Fácil de adicionar ou remover serviços sem reinicializar. | • Desempenho inferior devido à comunicação interprocessos. <br>• Requer mais recursos do sistema. |
| **Sistemas em Camadas** | • Organização e facilidade de manutenção pela estrutura modular. <br>• Segurança ao isolar a camada de hardware. | • Pode haver overhead nas interações entre camadas. <br>• Difícil de implementar sem impacto no desempenho. |
| **Sistemas Híbridos** | • Flexibilidade para otimizar desempenho e modularidade. <br>• Mistura os melhores aspectos de outras arquiteturas. | • Complexidade elevada, dificultando a depuração. <br>• Pode ter redundância de funções e aumentar o tamanho do núcleo. |
| **Máquinas Virtuais** | • Isolamento completo entre sistemas (guests). <br>• Flexibilidade para rodar múltiplos sistemas operacionais no mesmo hardware. | • Desempenho reduzido em comparação ao uso direto do hardware. <br>• Overhead devido à camada de virtualização (hypervisor). |
| **Contêineres** | • Desempenho elevado, já que compartilham o núcleo do host. <br>• Isolamento eficiente e menor overhead em comparação às máquinas virtuais. | • Menor isolamento em relação às máquinas virtuais. <br>• Vulnerabilidade compartilhada com o núcleo do sistema host. |
| **Sistemas Exonúcleo** | • Cada aplicação possui sua própria biblioteca de serviços. <br>• Redução de overhead no núcleo central. | • Complexidade em integrar e gerenciar bibliotecas separadas. <br>• Suporte limitado em comparação com sistemas tradicionais. |
| **Sistemas Uninúcleo** | • Alta eficiência em ambientes com requisitos específicos. <br>• Executa tudo em modo privilegiado. | • Menor segurança, pois não há divisão entre modo kernel e usuário. <br>• Menos flexível, adequado para aplicações dedicadas. |
<br>

2. O Linux possui um núcleo similar com o da figura 3.1, mas também possui “tarefas de núcleo” que executam como os gerentes da figura 3.2. Seu núcleo é monolítico ou micronúcleo? Por quê?

**Resposta:**  
<pre>
   O núcleo do Linux é considerado monolítico porque sua estrutura baseia-se em um único bloco de código que roda no espaço de núcleo e, por isso, permite que as operações tenham acesso direto e sem restrições entre si. Essa característica possibilita uma comunicação direta entre componentes, o que contribui para o desempenho e eficiência do sistema.  
   Embora o Linux incorpore algumas funcionalidades que se assemelham a sistemas micronúcleo, como a modularidade, elas são implementadas como módulos de kernel, que podem ser carregados e descarregados dinamicamente no núcleo, mas ainda rodam em modo kernel, com acesso a privilégios completos. Dessa forma, mesmo com a possibilidade de modularidade e a presença de "tarefas de núcleo", o Linux não atinge o nível de isolamento e segurança característicos de sistemas de micronúcleo, nos quais componentes principais rodam em espaço de usuário e se comunicam por meio de chamadas de sistema. Por isso, o Linux é classificado como um sistema de núcleo monolítico.
</pre>

3. Sobre as afirmações a seguir, relativas às diversas arquiteturas de sistemas operacionais, indique quais são incorretas, justificando sua resposta:  
   1. **Uma máquina virtual de sistema é construída para suportar uma aplicação escrita em uma linguagem de programação específica, como Java.**
   
<pre>Justificativa: Uma máquina virtual de sistema simula todo o ambiente de um sistema operacional, permitindo que vários sistemas operacionais completos sejam executados como convidados. Ela não é restrita a uma linguagem de programação específica. A descrição dada corresponde a uma máquina virtual de processo, que é construída para suportar uma aplicação em uma linguagem específica (por exemplo, a JVM para Java).</pre>

   2. Um hipervisor convidado executa sobre um sistema operacional hospedeiro.

   3. **Em um sistema operacional micronúcleo, os diversos componentes do sistema são construídos como módulos interconectados executando dentro do núcleo.**

<pre>Justificativa: Em sistemas operacionais com arquitetura micronúcleo, os principais componentes (como drivers, sistema de arquivos, etc.) são isolados e executados no espaço do usuário, não dentro do núcleo. O núcleo, ou micronúcleo, é minimalista e executa apenas as funções mais essenciais, como a comunicação entre processos e o gerenciamento básico de memória.</pre>

   4. **Núcleos monolíticos são muito utilizados devido à sua robustez e facilidade de manutenção.**

<pre>Justificativa: Núcleos monolíticos são utilizados principalmente devido ao desempenho, pois toda a comunicação e interação entre componentes é direta e ocorre no modo kernel. No entanto, eles são considerados mais difíceis de manter e menos robustos, já que um erro em um componente pode comprometer a estabilidade de todo o sistema.</pre>

   5. Em um sistema operacional micronúcleo, as chamadas de sistema são implementadas através de trocas de mensagens.