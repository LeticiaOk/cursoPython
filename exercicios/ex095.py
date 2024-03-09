"""
Aprimeore o desafio 093 para que ele funcione com 
vários jogadores. Incluindo um sistema de visualização
de detalhes do aproveitamennto de cada jogador
"""
# condicao = []
# jogadores = []
# lista_gols = []
# dados = {}
# total_gols = 0
# cont = 0
# while True:
#     dados["cod"] = cont

#     dados['nome'] = str(input('Nome do Jogador: '))
#     dados['partidas'] = int(input(f'Quantas partidas {dados["nome"]} jogou? '))

#     for c in range(dados['partidas']):
#         lista_gols.append(int(input(f'Quantos gols na partida {c}? ')))
#         total_gols+= lista_gols[c]
    
#     dados['gols'] = lista_gols[:]
#     dados['total'] = total_gols

   
#     jogadores.append(dados.copy())
#     dados.clear()
#     lista_gols.clear()
#     total_gols = 0

#     resp = str(input('Quer continuar? [S/N] ')).upper()
#     if resp == 'N':
#         break
#     else:
#         cont+=1

# print('-' * 30)
# print('cod nome gols total')
# print('-' * 30)
# for d in jogadores:
#     for v in d.values():
#         print(f'  {str(v):<15}', end=' ')
#     print()


# while True:
#     print('-' * 30)
#     resp = int(input('Mostrar dados de qual jogador? '))

#     while (resp > cont or resp < 0) and resp != 999:
#         resp = int(input(f'ERRO: Não existe jogador com o código {resp}! Tente novamente: '))

#     if resp == 999:
#         print('PROGRAMA ENCERRADO')
#         break

   
#     for d in jogadores:
#         if d["cod"] == resp:
#             print(f'-- LEVANTAMENTO DO JOGADOR {d["nome"]} --')
#             for c in range(d["partidas"]):
#                 print(f'   No jogo {c} fez {d["gols"][c]} gols.')


# for c in range(len(jogadores)):
#     for d in jogadores:
#         if d["nome"] not in condicao and c not in condicao:
#             print(f'{c} {d["nome"]:<10} {d["gols"]} {d["total"]:>10}')
#             condicao.append(d["nome"])
#             condicao.append(c)
           
# RESOLUÇÃO
time = list()
jogador = dict()
partidas = list()

while True:
    jogador.clear()
    jogador['nome'] =  str(input('Nome do Jogador: '))
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f'   Quantos gols na partida {c + 1}? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break
print('-' * 50)

print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()

print('-' * 50)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 50)

while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break 
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com código {busca}!')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]};')
        for i, g in enumerate(time[busca]['gols']):
            print(f'    No jogo {i + 1} fez {g} gols')
    print('-' * 50)
print('<< VOLTE SEMPRE >>')