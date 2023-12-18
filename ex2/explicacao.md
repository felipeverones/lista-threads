
# Explicação - Questão 2

Quando um processo filho é criado no sistema operacional através de uma chamada de sistema, como `os.fork()`, o sistema operacional faz uma cópia do espaço de memória do processo pai para o processo filho. Isso significa que, embora as variáveis inicialmente tenham os mesmos valores em ambos os processos (porque o filho é uma cópia do pai), alterações feitas a essas variáveis no processo filho não afetam o processo pai e vice-versa, devido à separação de memória.

### Resumo do que Acontece no Código

- **Processo Pai:**
  - Altera a variável `A` para 30 e exibe os valores antes e depois da alteração.
- **Processo Filho:**
  - Altera `A` para 20 e também exibe os valores antes e depois da alteração.

### Observações Importantes

- As alterações em `A` no processo filho não afetam `A` no processo pai e vice-versa, pois os processos não compartilham memória entre si.
- Esta característica é conhecida como **isolamento de processos** e é crucial para a estabilidade e segurança dos sistemas operacionais. 

### Importância do Isolamento de Processos

Se os processos pudessem compartilhar memória:
- Um processo poderia interferir involuntariamente em outro, causando erros e falhas no sistema.
- Um processo malicioso poderia interferir intencionalmente em outros processos, comprometendo a segurança do sistema.
