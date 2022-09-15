from datetime import date
# Criar função para validar entrada de valores




# Criar função pra validar números inteiros

def validanum(n):
    while True:
        try:
            n = int(n)
            return n
            break
        except ValueError:
            print('\033[31mErro\033[m')
            n = str(input('Digite um número válido: '))








