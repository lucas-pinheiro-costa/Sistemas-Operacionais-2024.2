/*Desenhe o diagrama de tempo da execução do código a seguir, informe qual a
saída do programa na tela (com os valores de x) e calcule a duração aproximada
de sua execução.*/

#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>

int main() {
    int x = 0;
    pid_t pid;

    pid = fork();  // Cria um processo filho

    if (pid < 0) {
        perror("Erro ao criar processo");
        return 1;
    } else if (pid == 0) {
        // Código para o processo filho
        x++;         // Incrementa x no processo filho
        sleep(5);
    } else {
        // Código para o processo pai
        wait(NULL);  // Pai espera pelo término do processo filho
        x++;         // Incrementa x no processo pai
        pid = fork();

        if (pid == 0) {
            // Novo processo filho criado pelo pai
            x++;
            sleep(5);
        } else {
            wait(NULL);  // Pai espera pelo segundo filho
        }
    }

    printf("Valor de x: %d\n", x);
    return 0;
}

/*
#include <stdio.h>
int main()
{
    int x = 0;

    fork();
    x++;
    sleep(5);
    wait(0);
    fork();
    wait(0);
    sleep(5);
    x++;
    printf("Valor de x: %d\n", x);
}
*/