"""
Crie um progrma onde 4 jogadores joguem um dado e 
tenham resultados aleatórios. Guarde esses resultados
em  um dicionário. No final, coloque esse dicionário
em ordem, sabendo que o vencedor tirou o maior número
no dado.
"""
# from random import randint
# from time import sleep

# jogo = {}
# condicao = []
# ordem = []

# # sorteando números 
# jogo['jogador1'] = randint(1,6)
# jogo['jogador2'] = randint(1,6)
# jogo['jogador3'] = randint(1,6)
# jogo['jogador4'] = randint(1,6)

# # mostrando valores dos jogadores
# for k, v in jogo.items():
#     print(f'{k} tirou {v}')
#     sleep(1)

# print('Ranking dos jogadores: ')

# # colocando valores em ordem na lista
# for v in jogo.values():
#     ordem.append(v)
# ordem.sort()
# ordem.sort(reverse=True)

# # mostrando valores em ordem
# cont = 0
# for i in range(len(ordem)):
#     for k, v in jogo.items():
#         if v == ordem[i] and k not in condicao:
#             cont+= 1
#             condicao.append(k)
#             print(f'{cont}º lugar: {k} com {v}')
#             sleep(1)

# RESOLUÇÃO
from random import randint
from time import sleep
from operator import itemgetter
jogo = {'jogador1':randint(1,6),
        'jogador2':randint(1,6),
        'jogador3':randint(1,6),
        'jogador4':randint(1,6)}
ranking = list()
print('Valores sorteados:')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)

ranking = sorted(jogo.items(),key=itemgetter(1), reverse=True)
print('-' * 30)
print('  == RANGINK DOS JOGADORES ==')
for i, v in enumerate(ranking):
    print(f'   {i+1}º lugar: {v[0]} com {v[1]}.')
    sleep(1)