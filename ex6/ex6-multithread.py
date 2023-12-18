import threading
import re
import time  # Importando a biblioteca time para medir o tempo

# Função para contar ocorrências de uma palavra em um texto
def conta_palavra(segmento, palavra_alvo, result_list):
    ocorrencias_segmento = len(re.findall(rf'\b{palavra_alvo}\b', segmento, re.IGNORECASE))
    result_list.append(ocorrencias_segmento)

# Lendo o conteúdo do arquivo de texto
with open("./ex4/texto.txt", "r", encoding="utf-8") as file:
    texto = file.read()

# Palavra a ser contada no texto
palavra_alvo = "IA"

# Dividindo o texto em três segmentos
length = len(texto)
part1 = texto[:length//3]
part2 = texto[length//3:2*length//3]
part3 = texto[2*length//3:]

# Lista para armazenar os resultados
resultados = []

# Marca o tempo de início
inicio_multi = time.time()

# Criando e iniciando as threads
t1 = threading.Thread(target=conta_palavra, args=(part1, palavra_alvo, resultados))
t2 = threading.Thread(target=conta_palavra, args=(part2, palavra_alvo, resultados))
t3 = threading.Thread(target=conta_palavra, args=(part3, palavra_alvo, resultados))

t1.start()
t2.start()
t3.start()

# Esperando todas as threads terminarem
t1.join()
t2.join()
t3.join()

# Somando as ocorrências encontradas em cada segmento
total_ocorrencias = sum(resultados)

# Marca o tempo de término
fim_multi = time.time()

# Calcula e exibe o tempo decorrido
tempo_multi = fim_multi - inicio_multi

# Exibindo a quantidade de ocorrências e o tempo
print(f"[Multithread] A palavra '{palavra_alvo}' aparece {total_ocorrencias} vezes no texto.")
print(f"[Multithread] Tempo de execução: {tempo_multi:.4f} segundos.")
