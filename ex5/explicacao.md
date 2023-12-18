
# Explicação - Questão 5

O objetivo da questão 5 é transformar o programa monothread da questão 4 em um programa multithread. 
Isso permite que a busca da palavra no texto seja feita simultaneamente em diferentes seções do arquivo, 
utilizando várias threads.

Aqui está uma explicação passo a passo do código:

1. **Importações Necessárias**:
    - `threading`: Usado para criar e gerenciar threads.
    - `re`: Módulo de expressões regulares usado para buscar a palavra no texto.
    
```python
import threading
import re
```

2. **Função `conta_palavra`**:
    - A função aceita um segmento de texto, uma palavra alvo e uma lista de resultados.
    - A função busca a palavra alvo no segmento de texto usando uma expressão regular.
    - O número de ocorrências encontradas é adicionado à lista de resultados.
    
```python
def conta_palavra(segmento, palavra_alvo, result_list):
    ocorrencias_segmento = len(re.findall(rf'\b{palavra_alvo}\b', segmento, re.IGNORECASE))
    result_list.append(ocorrencias_segmento)
```

3. **Leitura do Arquivo de Texto**:
    - O texto é lido de um arquivo e armazenado na variável `texto`.
    
```python
with open("./ex4/texto.txt", "r", encoding="utf-8") as file:
    texto = file.read()
```

4. **Divisão do Texto em Segmentos**:
    - O texto completo é dividido em três segmentos aproximadamente iguais.
    
```python
length = len(texto)
part1 = texto[:length//3]
part2 = texto[length//3:2*length//3]
part3 = texto[2*length//3:]
```

5. **Criação e Inicialização das Threads**:
    - Três threads são criadas, cada uma responsável por contar as ocorrências da palavra alvo em um dos segmentos.
    - As threads são iniciadas simultaneamente.
    
```python
t1 = threading.Thread(target=conta_palavra, args=(part1, palavra_alvo, resultados))
t2 = threading.Thread(target=conta_palavra, args=(part2, palavra_alvo, resultados))
t3 = threading.Thread(target=conta_palavra, args=(part3, palavra_alvo, resultados))

t1.start()
t2.start()
t3.start()
```

6. **Aguardando a Conclusão das Threads**:
    - O programa principal espera até que todas as três threads terminem sua execução.
    
```python
t1.join()
t2.join()
t3.join()
```

7. **Somando os Resultados**:
    - O número total de ocorrências da palavra alvo é calculado somando-se os resultados de cada thread.
    
```python
total_ocorrencias = sum(resultados)
```

8. **Exibindo o Resultado**:
    - O número total de ocorrências da palavra alvo é exibido.
    
```python
print(f"A palavra '{palavra_alvo}' aparece {total_ocorrencias} vezes no texto.")
```

A abordagem multithread permite que a busca seja realizada mais rapidamente, especialmente em arquivos de texto muito grandes, 
já que diferentes partes do texto são processadas simultaneamente.

---

