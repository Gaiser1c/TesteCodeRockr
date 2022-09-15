import funcoes as fc
import pendulum as pl

                                    # Gerenciamento de investimentos


        # Fazer input e validação dos dados

            # Nome ---> OK

nome = str(input('Digite o seu nome: '))


            # Valor do investimento ---> OK

valor_investimento = fc.valida_valor(str(input('Digite o valor que deseja investir? R$ ')))


            # Validar data da criação do investimento ---> OK

print('Digite a data da sua aplição no formato: AAAA/MM/DD ')

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
    break

data_investimento = pl.date(day=dia, month=mes, year=ano)
print(data_investimento)


            # Validar data de saque do investimento ---> OK
print('Digite a data que deseja fazer o saque de sua aplição no formato: AAAA/MM/DD ')
while True:

    ano2 = fc.valida_numero(str(input('ano: ')))        #tem que ser pelo menos 1 mês após a data do investimento

    while True:
        if ano2 < pl.today().year:
            print('\033[31m ERRO: A data não pode ser menor que a atual! \033[m')
            ano2 = fc.valida_numero(str(input('Digite um ano válido: ')))
        else:
            break

    mes2 = fc.valida_numero(str(input('Mês: ')))

    if ano2 > pl.today().year:
        while True:
            if mes2 > 12 or mes2 < 0:
                print(f'\033[31m ERRO: O mês {mes2} não é válido! \033[m')
                mes2 = fc.valida_numero(str(input('Digite um mês válido: ')))
            else:
                break
    elif ano2 == pl.today().year:
        while True:
            if mes2 < 0 or mes2 > 12:
                print(f'\033[31m ERRO: O mês {mes2} não é válido! \033[m')
                mes2 = fc.valida_numero(str(input('Digite um mês válido: ')))

            elif mes2 < pl.today().month:
                print('\033[31m ERRO: A data não pode ser menor que a atual! \033[m')
                mes2 = fc.valida_numero(str(input('Digite um mês válido: ')))
            else:
                break

    dia2 = fc.valida_numero(str(input('Dia: ')))

    if ano2 > pl.today().year:

        while True:
            if dia2 < 0 or dia2 > 31:
                print(f'\033[31m ERRO: O dia "{dia2}" não é válido! \033[m')
                dia2 = fc.valida_numero(str(input('Digite um dia válido: ')))
            else:
                break

    elif ano2 == pl.today().year:
        if mes2 > pl.today().month:
            while True:
                if dia2 < 0 or dia2 > 31:
                    print(f'\033[31m ERRO: O dia "{dia2}" não é válido! \033[m')
                    dia2 = fc.valida_numero(str(input('Digite um dia válido: ')))
                else:
                    break
        elif mes2 == pl.today().month:
            while True:
                if dia2 < 0 or dia2 > 31:
                    print(f'\033[31m ERRO: O dia "{dia2}" não é válido! \033[m')
                    dia2 = fc.valida_numero(str(input('Digite um dia válido: ')))
                elif dia2 < pl.today().day:
                    print('\033[31m ERRO: A data não pode ser menor que a atual! \033[m')
                    dia2 = fc.valida_numero(str(input('Digite um dia válido: ')))
                else:
                    break
    break

data_saque = pl.date(day=dia2, month=mes2, year=ano2)


# Calculo de quantos meses se passaram ---> OK

periodo = pl.period(data_investimento, data_saque)
meses = - 1
for c in periodo.range('months'):
    print(c)
    meses += 1

if meses <= 0:
    print('O seu dinheiro ainda não rendeu, pos ainda não completou 1 mês!')



taxa = 0.52

