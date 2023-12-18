import os

def meu_shell():
    while True:
        # Receber o comando do usuário
        comando_input = input("meu_shell> ")
        
        # Dividir o comando e os argumentos
        comando_args = comando_input.split()
        comando = comando_args[0]
        
        # Criar um processo filho
        pid = os.fork()
        
        # Verificar se estamos no processo filho
        if pid == 0:
            # Executar o comando
            os.execlp(comando, *comando_args) 
        else:
            # Esperar o processo filho terminar
            os.wait()

# Executar o shell
meu_shell()