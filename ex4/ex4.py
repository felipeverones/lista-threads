import re


# Lendo o conteúdo do arquivo de texto
with open("./ex4/texto.txt", "r", encoding="utf-8") as file:
    texto = file.read()

# Palavra a ser contada no texto
palavra_alvo = "IA"

# Contando a quantidade de ocorrências da palavra no texto usando regex para considerar diferentes contextos
ocorrencias = len(re.findall(rf'\b{palavra_alvo}\b', texto, re.IGNORECASE))

# Exibindo a quantidade de ocorrências
print(f"A palavra '{palavra_alvo}' aparece {ocorrencias} vezes no texto.")