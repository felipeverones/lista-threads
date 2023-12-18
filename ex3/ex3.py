
import threading

# Variável global A
A = 10

def funcao_thread():
    global A
    print("\n[Thread Filho]")
    print("Valor original de A no thread filho:", A)
    A = 20  # Alterando o valor de A no thread filho
    print("Valor de A após alteração no thread filho:", A)

# Criando e iniciando o thread filho
thread_filho = threading.Thread(target=funcao_thread)
thread_filho.start()
thread_filho.join()

# Código no thread pai
print("\n[Thread Pai]")
print("Valor original de A no thread pai:", A)
A = 30  # Alterando o valor de A no thread pai
print("Valor de A após alteração no thread pai:", A)
