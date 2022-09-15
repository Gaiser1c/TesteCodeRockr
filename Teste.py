import funcoes as fc
import pendulum as pl

                                    # Gerenciamento de investimentos


        # Fazer input e validação dos dados

# Nome
nome = str(input('Digite o seu nome: '))




# Valor do investimento

valor_investimento = fc.valida_valor(str(input('Digite o valor que deseja investir? R$ ')))








# Data de Criação/ Validar datas

print('Digite a data na sua aplição no formato: AAAA/MM/DD ')
while True:

    ano = fc.valida_numero(str(input('ano: ')))

    while True:
        if ano > pl.today().year:
            print('\033[31m ERRO: A data não pode ser maior que a atual! \033[m')
            ano = fc.valida_numero(str(input('Digite um ano válido: ')))
        else:
            break

    mes = fc.valida_numero(str(input('Mês: ')))

    if ano < pl.today().year:
        while True:
            if mes > 12 or mes < 0:
                print(f'\033[31m ERRO: O mês {mes} não é válido! \033[m')
                mes = fc.valida_numero(str(input('Digite um mês válido: ')))
            else:
                break
    else:
        while True:
            if mes > 12 or mes < 0:
                print(f'\033[31m ERRO: O mês {mes} não é válido! \033[m')
                mes = fc.valida_numero(str(input('Digite um mês válido: ')))
            elif mes > pl.today().month:
                print('\033[31m ERRO: A data não pode ser maior que a atual! \033[m')
                mes = fc.valida_numero(str(input('Digite um mês válido: ')))
            else:
                break

    dia = fc.valida_numero(str(input('Dia: ')))

    if ano < pl.today().year:

        while True:
            if dia < 0 or dia > 31:
                print(f'\033[31m ERRO: O dia "{dia}" não é válido! \033[m')
                dia = fc.valida_numero(str(input('Digite um dia válido: ')))
            else:
                break

    else:
        if mes < pl.today().month:
            while True:
                if dia < 0 or dia > 31:
                    print(f'\033[31m ERRO: O dia "{dia}" não é válido! \033[m')
                    dia = fc.valida_numero(str(input('Digite um dia válido: ')))
                else:
                    break
        else:
            while True:
                if dia < 0 or dia > 31:
                    print(f'\033[31m ERRO: O dia "{dia}" não é válido! \033[m')
                    dia = fc.valida_numero(str(input('Digite um dia válido: ')))
                elif dia > pl.today().day:
                    print('\033[31m ERRO: A data não pode ser maior que a atual! \033[m')
                    dia = fc.valida_numero(str(input('Digite um dia válido: ')))
                else:
                    break



# Fazer calculos


taxa = 0.52

# Impostos
# Menos de 1 ano: 22,5%
# Entr 1 e 2 anos: 18,5%
# De 2 anos ou mais: 15%
