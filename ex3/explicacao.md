
# Explicação - Questão 3

## Sobre o Código 

1. **Thread Filho:**
   - O valor inicial de `A` é 10.
   - `A` é alterado para 20.
   - **Observação:** Quando alteramos `A` no thread filho, estamos alterando a mesma instância de `A` que o thread pai vê, pois threads **compartilham memória**.

2. **Thread Pai (Thread Principal):**
   - Após o thread filho ser executado (pois usamos `thread_filho.join()` para esperar o filho terminar), o valor de `A` é 20 (modificado pelo filho).
   - `A` é alterado para 30 pelo thread pai.
   - Assim, `A` foi novamente modificado na memória compartilhada, afetando o que seria visto por outros threads (se existissem e fossem executados posteriormente).

## Diferenças Essenciais entre Threads e Processos

- **Memória Compartilhada:**
  - **Threads:** Compartilham memória. Uma alteração em uma variável global em um thread afeta essa variável em todos os outros threads.
  - **Processos:** Não compartilham memória. Alterações em variáveis no processo filho não afetam o processo pai e vice-versa.

- **Overhead:**
  - **Threads:** Geralmente têm menos overhead (custo adicional para gerenciamento) do que os processos porque compartilham recursos e o contexto de troca entre threads (do mesmo processo) é geralmente mais leve.
  - **Processos:** Tendem a ter mais overhead, pois cada processo tem seu próprio espaço de memória e a troca de contexto entre processos é mais pesada.

- **Uso:**
  - **Threads:** São úteis quando queremos realizar tarefas paralelas que precisam acessar/modificar as mesmas variáveis.
  - **Processos:** São úteis para isolar completamente tarefas, dando a cada uma seu próprio espaço de memória.

## Observação sobre Concorrência (pode cair na prova)

Quando usamos threads, é crucial estar ciente dos problemas potenciais de concorrência (como condições de corrida) devido ao acesso compartilhado à memória. Pode ser necessário usar mecanismos de sincronização (como locks) para garantir a execução correta.
