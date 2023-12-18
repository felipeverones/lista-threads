
# Explicação - Questão 4

O código realiza a busca e contagem de ocorrências de uma palavra específica (neste caso, "IA") em um texto. 

1. **Leitura do Arquivo de Texto:**
   O código começa lendo um arquivo de texto utilizando o método `open()` e armazena o conteúdo lido na variável `texto`. 
   ```python
   with open("ex4/texto.txt", "r", encoding="utf-8") as file:
       texto = file.read()
   ```
   O uso de `with open()` garante que o arquivo seja fechado após a leitura, e o parâmetro `encoding="utf-8"` garante que caracteres especiais sejam lidos corretamente.

2. **Definição da Palavra-Alvo:**
   A palavra que deseja-se contar no texto é definida na variável `palavra_alvo`.
   ```python
   palavra_alvo = "IA"
   ```
   
3. **Busca e Contagem com Expressão Regular:**
   Utilizo expressões regulares (regex) para encontrar todas as ocorrências da palavra-alvo no texto, sem considerar a diferença entre letras maiúsculas e minúsculas. A função `re.findall()` retorna todas as ocorrências da palavra que satisfazem o padrão da expressão regular. `\b` indica a borda da palavra, garantindo que palavras que contenham a palavra-alvo não sejam contadas.
   ```python
   ocorrencias = len(re.findall(rf'\b{palavra_alvo}\b', texto, re.IGNORECASE))
   ```
   
4. **Exibição do Resultado:**
   Por fim, o código exibe a quantidade de ocorrências encontradas utilizando a função `print()`.
   ```python
   print(f"A palavra '{palavra_alvo}' aparece {ocorrencias} vezes no texto.")
   ```
   
Este código é executado de forma sequencial, ou seja, é monothread, cumprindo assim os requisitos da **Questão 4**.
