import funcoes as fc
import pendulum as pl

                                        #GERENCIAMENTO DE INVESTIMENTOS CODEROCKER



# Variáveis
nome = 0
valor_investimento = 0
data_investimento = 0
data_saque = 0
lucro = 0
impostos = 0
saldo_liquido = 0



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



                                        # Calculo



            # Calculo de quantos meses se passaram ---> OK

periodo = pl.period(data_investimento, data_saque)
meses = - 1
for c in periodo.range('months'):
    meses += 1


            # Calculo de Quanto o dinheiro já rendeu --->

if meses <= 0:
    dias = pl.period(data_investimento, data_saque)
    print(f'O seu dinheiro ainda não rendeu, pois se passaram somente {dias} dias!')

else:
    montante = valor_investimento
    for c in range(meses):
        montante = montante + (montante * 0.52/100)

    lucro = montante - valor_investimento
    impostos = lucro - fc.imposto(lucro, meses)
    saldo_liquido = montante - impostos




                                        # Formatação dos dados



            # Agrupar os dados em um cadastro --->

dados_cliente = {
    'nome': nome,
    'valor_investimento': valor_investimento,
    'data_investimento': data_investimento,
    'data_saque': data_saque,
    'lucro': lucro,
    'impostos': impostos,
    'saldo_liquido': saldo_liquido
}

            # Formatar os dados para que fiquem de forma legível no terminal ---> OK


print(f'\033[4;7m{"Banco CodeRockr":^40}\033[m')
print('-' * 40)
print(f'{"Dados bancários:":^40}')
print('-' * 40)

print(f'{"Nome:"} {dados_cliente["nome"]:>34}')
print(f'{"Valor aplicado:"} {dados_cliente["valor_investimento"]:24.2f}')
print(f'{"Data da aplicação:":<29} {dados_cliente["data_investimento"]}')
print(f'{"Data do saque:":<29} {dados_cliente["data_saque"]}')
print(f'{"Lucro:"} {dados_cliente["lucro"]:>33.2f}')
print(f'{"Impostos:"} {dados_cliente["impostos"]:>30.2f}')
print(f'{"Saldo Liquido:"} {dados_cliente["saldo_liquido"]:>25.2f}')





