"""
Crie um programa que leia:

NOME
SEXO
IDADE

de várias pessoas, guardando os dados de cada pessoa
em um dicionário e todos o dicionários em uma lista.
No final mostre:

A) QUANTAS PESSOAS FORAM CADASTRADAS
B) A MÉDIA DE IDADE DO GRUPO
C) UMA LISTA COM TODAS AS MULHERES
D) UMA LISTAS COM TODAS AS PESSOAS ACIMA DA MÉDIA
"""
# # Declarando variáveis
# cadastros = []
# dados = {}
# media = 0

# # Preenchendo e lendo o fomulário
# while True:

#     dados['nome'] = str(input('Nome: '))
#     dados['sexo'] = str(input('Sexo: [M/F] ')).upper()
#     dados['idade'] = int(input('Idade: '))
#     cadastros.append(dados.copy())
#     dados.clear()
#     resp = str(input('Deseja continuar? [S/N] ')).upper()
#     if resp == 'N':
#         break

# print('-' * 50)
# # Mostrando o úmero total de pessoas do grupo
# print(f' - O grupo tem {len(cadastros)} pessoas')

# # Calculando a média de idade do grupo
# for c in cadastros:
#         media += c['idade']
# media = media/len(cadastros) # calculando média
# print(f' - A média de idade é de {media} anos')

# # Listando o nome das mulheres do grupo
# print(f' - A lista de mulheres cadastradas foram: ', end='')

# for c in cadastros:
#      if c['sexo'] == 'F':
#           print(c['nome'], end=' ')
# print()

# #Listando pessoas acima da média de idade do grupo
# print(f' - Lista de pessoas que estão acima da média:\n')

# for c in cadastros:
#     for k, v in c.items():
#         if c['idade'] > media:
#             print(f'{k} = {v}', end='; ')
#     print()

# RESOLUÇÃO
galera = list()
pessoa = dict()
soma = media= 0
while True:
    pessoa.clear
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break 
        print('ERRO! Por favor, digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa["idade"]
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas  S ou N.')
    if resp == 'N':
        break
print('-' * 60)
print(f'A) Ao todo temos {len(galera)} pessoas cadastradas')
media = soma / len(galera)
print(f'B) A média de idade é de {media:5.2f} anos.')
print('C) As mulheres cadastradas foram ', end='')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]} ',end='')
print()

print('D) Lista das pessoas que estão acima da média:')
for p in galera:
    if p['idade'] >= media:
        print('    ', end='')
        for k, v in p.items():
            print(f'{k} = {v}: ', end='')
        print()
print('<< ENCERRADO >>')