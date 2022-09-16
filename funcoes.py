import pendulum as pl



# Criar função para validar entrada de valores---> OK
def valida_valor(n):
    """ Esta função é utilizada para que apenas valores monetários válidos sejam aceitos. """

    while True:

        if ',' in n:
            n.strip()
            n = n.replace(',', '.')
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



# Criar função pra validar números inteiros ---> OK

def valida_numero(n):
    """ Esta função foi criada para que apenas números inteiros sejam aceitos."""
    while True:
        try:
            n = int(n)
            return n
            break
        except ValueError:
            print('\033[31mErro\033[m')
            n = str(input('Digite um número válido: '))



# Criar uma função para calcular o imposto ---> OK

def imposto(lucro, meses):

    """ Esta função foi criada para calcular o imposto de acordo com o tempo de investimento. """
    if meses > 24:
        lucro = lucro - (lucro * (15/100))
        return lucro

    elif 12 <= meses <= 24:
        lucro = lucro - (lucro * (18.5/100))
        return lucro

    else:
        lucro = lucro - (lucro * (22.5/100))
        return lucro








