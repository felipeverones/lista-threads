import re
import time  # Importando a biblioteca time para medir o tempo

# Lendo o conteúdo do arquivo de texto
with open("./ex4/texto.txt", "r", encoding="utf-8") as file:
    texto = file.read()

# Palavra a ser contada no texto
palavra_alvo = "IA"

# Marca o tempo de início
inicio_mono = time.time()

# Contando a quantidade de ocorrências da palavra no texto usando regex para considerar diferentes contextos
ocorrencias = len(re.findall(rf'\b{palavra_alvo}\b', texto, re.IGNORECASE))

# Marca o tempo de término
fim_mono = time.time()

# Calcula e exibe o tempo decorrido
tempo_mono = fim_mono - inicio_mono

# Exibindo a quantidade de ocorrências e o tempo
print(f"[Monothread] A palavra '{palavra_alvo}' aparece {ocorrencias} vezes no texto.")
print(f"[Monothread] Tempo de execução: {tempo_mono:.4f} segundos.")
