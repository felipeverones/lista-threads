
# Explicação - Questão 1

### Código de um Shell Simples

```python
import os

def meu_shell():
    while True:
        comando_input = input("meu_shell> ")
        comando_args = comando_input.split()
        comando = comando_args[0]
        pid = os.fork()
        if pid == 0:
            os.execlp(comando, *comando_args)
        else:
            os.wait()

meu_shell()
```

### Explicação

1. **Importação do Módulo OS:**
   O módulo `os` no Python fornece uma maneira de usar funcionalidades dependentes do sistema operacional, como ler ou escrever no sistema de arquivos, iniciar ou matar processos, etc.

2. **Definição da Função Shell:**
   Crio uma função chamada `meu_shell` para encapsular a lógica do shell. Isso ajuda a manter o código organizado e permite que o shell seja iniciado chamando uma função.

3. **Loop Infinito:**
   O `while True:` cria um loop infinito que continuará solicitando comandos do usuário até que o programa seja interrompido (por exemplo, com Ctrl+C).

4. **Entrada do Usuário:**
   `input("meu_shell> ")` exibe um prompt para o usuário e espera que um comando seja inserido. O comando inserido é armazenado como uma string na variável `comando_input`.

5. **Separação de Comando e Argumentos:**
   `comando_input.split()` divide a string do comando_input em uma lista, utilizando espaço como delimitador. O comando (primeira palavra) e os argumentos (palavras subsequentes, se houver) são separados e armazenados em `comando_args`. `comando` armazena o nome do comando a ser executado.

6. **Criação de Processo Filho:**
   `os.fork()` cria um processo filho. A partir deste ponto, tanto o processo pai quanto o filho começarão a executar do mesmo ponto no código, mas o valor retornado de `os.fork()` ajudará a distinguir entre eles.

7. **Execução de Comando no Processo Filho:**
   Se `pid == 0`, significa que estamos no processo filho. `os.execlp(comando, *comando_args)` substitui o processo filho pelo comando que queremos executar. `comando` é o nome do programa que queremos executar e `*comando_args` são os argumentos que passamos para o programa.

8. **Espera pelo Processo Filho no Processo Pai:**
   Se `pid` não é `0`, estamos no processo pai. `os.wait()` faz com que o processo pai espere o processo filho terminar antes de continuar.

9. **Início do Shell:**
   Finalmente, chamamos a função `meu_shell()` para iniciar o shell.





# Explicação adicional para revisão para prova

- **Processo Pai (Shell):**
  - O processo pai, que é o nosso shell personalizado no código, é o processo que interage com o usuário, solicitando e recebendo comandos.
  - O processo pai permanece em execução e entra em um estado de espera quando um comando está sendo executado para, em seguida, retornar ao usuário quando o comando é concluído.
  - Basicamente, ele aguarda o comando do usuário, cria um processo filho para executar o comando e espera o processo filho terminar.

- **Processo Filho (Comando Executado):**
  - O processo filho é criado para executar o comando especificado pelo usuário.
  - Quando um comando é dado através do shell, o processo pai (shell) cria um processo filho usando `fork()`. Este processo filho é uma cópia do processo pai mas executa o comando desejado do usuário usando `execlp()`.
  - `execlp()` substitui a imagem do processo filho (que é uma cópia do pai) pela imagem do comando a ser executado. Dessa forma, o processo filho se torna o processo do comando a ser executado.
  - Uma vez que o comando (agora o processo filho) é concluído, ele termina e o controle retorna para o processo pai (o shell).

Por exemplo, se você digitar um comando como `ls` no shell criado, o seguinte acontece:

1. **O processo pai (shell) permanece ativo e esperando por comandos do usuário.**
2. **Quando `ls` é digitado:**
   - O processo pai cria um processo filho com `fork()`.
   - No processo filho, `execlp()` substitui a imagem do processo pelo comando `ls`, e `ls` é executado.
   - O processo pai espera o filho terminar com `wait()`.
3. **Uma vez que `ls` (processo filho) termina a execução, o controle retorna ao shell (processo pai), que volta a esperar por mais comandos do usuário.**

Essa separação entre processo pai e filho permite que o shell execute comandos consecutivamente e isola a execução de cada comando em seu próprio processo, evitando que um comando que falhe ou seja interrompido afete o shell.
