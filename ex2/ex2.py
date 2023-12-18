import os

# Variável global A
A = 10

# Criando um processo filho com fork()
pid = os.fork()

# Código que será executado pelo processo filho
if pid == 0:
    print("\n[Processo Filho]")
    print("Valor original de A no processo filho:", A)
    A = 20  # Alterando o valor de A no processo filho
    print("Valor de A após alteração no processo filho:", A)

# Código que será executado pelo processo pai
else:
    print("\n[Processo Pai]")
    print("Valor original de A no processo pai:", A)
    A = 30  # Alterando o valor de A no processo pai
    print("Valor de A após alteração no processo pai:", A)
    os.wait()  # Esperando o processo filho terminar
