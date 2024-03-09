"""
Faça um programa que tenha uma função chamada
ficha(), que receba dois parâmetros opcionais:
o nome de um jogador e quantos gols ele marcou.

O programa deverá ser capaz de mostrar a ficha do
jogador, mesmo que algum dado não tenha sido 
informado corretamente
"""

# def ficha(nome = 'UNKNOWN', gols = 0):
#     if nome.isspace() == True or nome == '':
#         nome = 'UNKNOWN'
#     if  gols.isspace() == True or gols == '' or gols.isnumeric() ==  False:
#         gols = '0'

#     return f'O jogador {nome} fez {gols} gol(s) no campeonato'


# # Porgrama Principal
# put_nome = str(input('Nome do jogador: '))
# put_gols = str(input('Número de gols: '))
# print(ficha(put_nome, put_gols))

# RESOLUÇÃO
def ficha(jog='<desconhecido>', gol=0):
    print(f'O jogador {jog} fez {gol} gol(s) no campeonato')

# Programa principal
n = str(input('Nome do jogador: '))
g = str(input('Número de Gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gol=g)
else:
    ficha(n, g)
