"""
Crie um programa que gerencia o aproveitamento de um
jogador de futebol. O programa vai ler:

NOME DO JOGADOR
QUANTAS PARTIDAS ELE JOGOU
QUANTIDADE DE GOLS FEITOS EM CADA PARTIDA

No final, tudo isso será quardado em um dicionário,
incluindo o TOTAL DE GOLS feitos durante o campeonato
"""

# dados = {}
# lista_gols = []
# total_gols = 0

# # Preenchendo e lendo formulário
# dados['nome'] = str(input('Nome do Jogador: '))
# partidas =  int(input(f'Quantas partidas {dados["nome"]} jogou? '))

# # Preenchendo o número de gols de cada partida
# for c in range(partidas):
#     lista_gols.append(int(input(f'Quantos gols na partida {c}? ')))
#     total_gols+=lista_gols[c] # total de gols

# dados['gols'] = lista_gols # adcionando a lista
# dados['total'] = total_gols # adicionando ao dicionário

# print('-' * 50)
# # mostrando dicionário 
# print(dados)

# print('-' * 50)

# # mostrando dados do dicionário com seus respectivos valores
# for k, v in dados.items():
#     print(f'O campo {k} tem o valor {v}.')

# print('-' * 50)

# # motrando número total de partidas jogadas
# print(f'O jogador {dados["nome"]} jogou {partidas} partidas.')

# # motrando a quantidade de gols de cada partida
# for c in range(partidas):
#     print(f' > Na partida {c}, fez {lista_gols[c]} gols.')

# # motrando número total de gols 
# print(f'Foi um total de {total_gols} gols.')

# RESOLUÇÃO
jogador = dict()
partidas = list()
jogador['nome'] =  str(input('Nome do Jogador: '))
tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for c in range(0, tot):
    partidas.append(int(input(f'   Quantos gols na partida {c}? ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print('-' * 60)
print(jogador)
print('-' * 60)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-' * 60)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
for i, v in enumerate(jogador['gols']):
    print(f'   => Na partida {i}, fez {v} gols.')
print(f'Foi um total de {jogador["total"]} gols.')