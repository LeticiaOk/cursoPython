"""
Crie um programa que leia: 

NOME
ANO DE NASCIMENTO
CARTEIRA DE TRABALHO

e cadastre-os(com IDADE) em um dicionário se por acaso
o CTPS for diferente de ZERO, o dicionário receberá
também:

ANO DE CONTRATAÇÃO
SALÁRIO

Calcule e acrescente além da IDADE:
COM QUANTOS ANOS A PESSOA VAI SE APOSENTAR

"""


# cadastro = {}
# # preenchendo formulário
# cadastro['nome'] = input(str('Nome: '))

# from datetime import date
# ano = date.today().year # importando ano atual
# ano_nasc = int(input('Ano de Nascimento: '))
# cadastro['idade'] = (ano - ano_nasc) # calculando idade

# cadastro['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))

# # preenchendo o  resto formário caso a condisão seja verdadeira
# if cadastro['ctps'] != 0:
#     cadastro['contratacao'] = int(input('Ano de contratação: '))
#     cadastro['salario'] = int(input('Salário: R$ '))
#     cadastro['aposentadoria'] = (35 - (ano - cadastro['contratacao'])) + cadastro['idade'] # calculando idade de aposentadoria

# print('-' * 50)
# # motrando dicionário
# print(cadastro)
# # motrando dados do dicionário com seus respectivos valores
# for k, v in cadastro.items():
#     print(f'{k} tem o valor {v} ')

#RESOLUÇÃO
from datetime import datetime
dados = {}
dados['nome'] = str(input('Nome: '))
nasc = int(input('Ano de nascimento: '))
dados['idade'] = datetime.now().year - nasc
dados['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if dados['ctps'] != 0:
    dados['contratacao'] = int(input('Ano de Contratação: '))
    dados['salario'] = float(input('Salário: R$ '))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratacao'] + 35) - datetime.now().year)
print('-' * 60)
for k, v in dados.items():
    print(f'  - {k} tem o valor {v}')