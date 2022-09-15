from datetime import date
# Criar função para validar entrada de valores

def valida_valor(n):

    while True:

        if ',' in n:
            n.strip()
            n.replace(',', '.')
        else:
            n.strip()

        try:
            num = float(n)
        except ValueError:
            print('\033[31m ERRO: O valor é inválido! \033[m')
            n = str(input('Digite um valor válido: '))
            continue

        else:
            if num < 0:
                print('\033[31m ERRO: O valor não pode ser negativo! \033[m')
                n = str(input('Digite um valor válido: '))
                continue
            elif num == 0:
                print('\033[31m ERRO: o valor não pode ser igual a 0! \033[m')
                n = str(input('Digite um valor válido: '))
                continue
            else:
                return num
                break








# Criar função pra validar números inteiros

def valida_numero(n):
    while True:
        try:
            n = int(n)
            return n
            break
        except ValueError:
            print('\033[31mErro\033[m')
            n = str(input('Digite um número válido: '))






print(valida_valor(str(input())))
