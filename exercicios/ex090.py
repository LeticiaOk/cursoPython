""""
Faça um programa que leia o nome e médiade um aluno,
guardando também a situação em um dicionário.
No final, mostre o conteúdo da estrutura na tela 
"""

# boletim = {}

# boletim['Nome'] = str(input('Nome: '))
# boletim['Média'] = float(input('Média: '))

# if boletim['Média'] >= 6:
#     boletim['Situacão'] = 'Aprovado'
# else:
#     boletim['Situacão'] = 'Reprovado'

# for k, v in boletim.items():
#     print(f'{k} é igual a {v}')

# RESOLUÇÃO

aluno = {}
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))
if aluno['media'] >= 7:
    aluno['situacao'] = 'Aprovado'
elif 5 <= aluno['media'] < 7:
    aluno['situacao'] = 'Recuperação'
else:
    aluno['situacao'] = 'Reprovado'
print('-' * 30)
for k, v in aluno.items():
    print(f'  -{k} é igual a {v}')