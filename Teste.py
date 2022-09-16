import funcoes as fc
import pendulum as pl

                                        #GERENCIAMENTO DE INVESTIMENTOS CODEROCKER



# Variáveis
nome = 0
valor_investimento = 0
data_investimento = 0
data_saque = 0
lucro = 0
montante = 0
impostos = 0
saldo_liquido = 0
dia_saque = 0
dia_investimento = 0
mes_saque = 0
mes_investimento = 0
ano_saque = 0
ano_investimento = 0





                                        # Fazer input e validação dos dados



            # Nome ---> OK

nome = str(input('Digite o seu nome: '))


            # Valor do investimento ---> OK

valor_investimento = fc.valida_valor(str(input('Digite o valor que deseja investir? R$ ')))


            # Validar data da criação do investimento ---> OK

print('Digite a data da sua aplição no formato: AAAA/MM/DD ')

while True:

    ano_investimento = fc.valida_numero(str(input('ano: ')))

    while True:
        if ano_investimento > pl.today().year:
            print('\033[31m ERRO: A data não pode ser maior que a atual! \033[m')
            ano_investimento = fc.valida_numero(str(input('Digite um ano válido: ')))
        else:
            break

    mes_investimento = fc.valida_numero(str(input('Mês: ')))

    if ano_investimento < pl.today().year:
        while True:
            if mes_investimento > 12 or mes_investimento < 0:
                print(f'\033[31m ERRO: O mês {mes_investimento} não é válido! \033[m')
                mes_investimento = fc.valida_numero(str(input('Digite um mês válido: ')))
            else:
                break
    else:
        while True:
            if mes_investimento > 12 or mes_investimento < 0:
                print(f'\033[31m ERRO: O mês {mes_investimento} não é válido! \033[m')
                mes_investimento = fc.valida_numero(str(input('Digite um mês válido: ')))
            elif mes_investimento > pl.today().month:
                print('\033[31m ERRO: A data não pode ser maior que a atual! \033[m')
                mes_investimento = fc.valida_numero(str(input('Digite um mês válido: ')))
            else:
                break

    dia_investimento = fc.valida_numero(str(input('Dia: ')))

    if ano_investimento < pl.today().year:

        while True:
            if dia_investimento < 0 or dia_investimento > 31:
                print(f'\033[31m ERRO: O dia "{dia_investimento}" não é válido! \033[m')
                dia_investimento = fc.valida_numero(str(input('Digite um dia válido: ')))
            else:
                break

    else:
        if mes_investimento < pl.today().month:
            while True:
                if dia_investimento < 0 or dia_investimento > 31:
                    print(f'\033[31m ERRO: O dia "{dia_investimento}" não é válido! \033[m')
                    dia_investimento = fc.valida_numero(str(input('Digite um dia válido: ')))
                else:
                    break
        else:
            while True:
                if dia_investimento < 0 or dia_investimento > 31:
                    print(f'\033[31m ERRO: O dia "{dia_investimento}" não é válido! \033[m')
                    dia_investimento = fc.valida_numero(str(input('Digite um dia válido: ')))
                elif dia_investimento > pl.today().day:
                    print('\033[31m ERRO: A data não pode ser maior que a atual! \033[m')
                    dia_investimento = fc.valida_numero(str(input('Digite um dia válido: ')))
                else:
                    break
    break

data_investimento = pl.date(day=dia_investimento, month=mes_investimento, year=ano_investimento)
print(data_investimento)


            # Validar data de saque do investimento ---> OK

print('Digite a data que deseja fazer o saque de sua aplição no formato: AAAA/MM/DD ')
while True:

    ano_saque = fc.valida_numero(str(input('ano: ')))

    while True:
        if ano_saque > pl.today().year:
            print('\033[31m ERRO: A data de saque não pode ser maior que a atual! \033[m')
            ano_saque = fc.valida_numero(str(input('Digite um ano válido: ')))
        if ano_saque < ano_investimento:
            print('\033[31m ERRO: A data de saque não pode ser menor que a data do investimento! \033[m')
            ano_saque = fc.valida_numero(str(input('Digite um ano válido: ')))
        else:
            break

    mes_saque = fc.valida_numero(str(input('Mês: ')))

    if ano_saque == ano_investimento:
        while True:
            if mes_saque < 0 or mes_saque > 12:
                print(f'\033[31m ERRO: O mês {mes_saque} não é válido! \033[m')
                mes_saque = fc.valida_numero(str(input('Digite um mês válido: ')))

            elif mes_saque < mes_investimento:
                print('\033[31m ERRO: A data de saque não pode ser menor que a data do investimento! \033[m')
                mes_saque = fc.valida_numero(str(input('Digite um mês válido: ')))
            else:
                break

    elif ano_saque < pl.today().year:
        while True:
            if mes_saque < 0 or mes_saque > 12:
                print(f'\033[31m ERRO: O mês {mes_saque} não é válido! \033[m')
                mes_saque = fc.valida_numero(str(input('Digite um mês válido: ')))
            else:
                break
    elif ano_saque == pl.today().year:
        while True:
            if mes_saque < 0 or mes_saque > 12:
                print(f'\033[31m ERRO: O mês {mes_saque} não é válido! \033[m')
                mes_saque = fc.valida_numero(str(input('Digite um mês válido: ')))

            elif mes_saque > pl.today().month:
                print('\033[31m ERRO: A data de saque não pode ser maior que a atual! \033[m')
                mes_saque = fc.valida_numero(str(input('Digite um mês válido: ')))
            else:
                break

    dia_saque = fc.valida_numero(str(input('Dia: ')))

    if ano_saque == ano_investimento:
        while True:
            if mes_saque < 0 or mes_saque > 12:
                print(f'\033[31m ERRO: O mês {mes_saque} não é válido! \033[m')
                mes_saque = fc.valida_numero(str(input('Digite um mês válido: ')))
            elif mes_saque == mes_investimento:
                while True:
                    if dia_saque < 0 or dia_saque > 31:
                        print(f'\033[31m ERRO: O dia "{dia_saque}" não é válido! \033[m')
                        dia_saque = fc.valida_numero(str(input('Digite um dia válido: ')))
                    elif dia_saque < dia_investimento:
                        print('\033[31m ERRO: A data de saque não pode ser menor que a data do investimento! \033[m')
                        dia_saque = fc.valida_numero(str(input('Digite um dia válido: ')))
                    else:
                        break
            else:
                break

    elif ano_saque < pl.today().year:
        while True:
            if dia_saque < 0 or dia_saque > 31:
                print(f'\033[31m ERRO: O dia "{dia_saque}" não é válido! \033[m')
                dia_saque = fc.valida_numero(str(input('Digite um dia válido: ')))
            else:
                break
    elif ano_saque == pl.today().year:
        if mes_saque < pl.today().month:
            while True:
                if dia_saque < 0 or dia_saque > 31:
                    print(f'\033[31m ERRO: O dia "{dia_saque}" não é válido! \033[m')
                    dia_saque = fc.valida_numero(str(input('Digite um dia válido: ')))
                else:
                    break
        elif mes_saque == pl.today().month:
            while True:
                if dia_saque < 0 or dia_saque > 31:
                    print(f'\033[31m ERRO: O dia "{dia_saque}" não é válido! \033[m')
                    dia_saque = fc.valida_numero(str(input('Digite um dia válido: ')))
                elif dia_saque > pl.today().day:
                    print('\033[31m ERRO: A data de saque não pode ser maior que a atual! \033[m')
                    dia_saque = fc.valida_numero(str(input('Digite um dia válido: ')))
                else:
                    break
    break

data_saque = pl.date(day=dia_saque, month=mes_saque, year=ano_saque)



                                        # Calculos



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
if saldo_liquido == 0:
    saldo_liquido = valor_investimento


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



