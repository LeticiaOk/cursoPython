# jogos = 0
# numeros = []
# novo = 0
# jogos_lista = []
# jogos = int(input('Quantos jogos você quer gerar? '))

# from random import randint
# for c in range(0, jogos):
#     numeros = [randint(1,60),randint(1,60),randint(1,60),randint(1,60),randint(1,60),randint(1,60)]
#     for i in range(len(numeros)):
#         if numeros[i] not in jogos_lista:
#             jogos_lista.append(numeros[i])
#         else:
#             while numeros[i] in jogos_lista:
#                 numeros[i]= randint(1,60)
#             jogos_lista.insert(i,numeros[i])
#     print(jogos_lista)
#     jogos_lista.clear()

# RESOLUÇÃO

from random import randint
from time import sleep
lista = list()
jogos = list()
print('-' * 30)
print('      JOGA NA MEGA SENA      ')
print('-' * 30)
quant = int(input('Quantos jogos você quer que eu sorteie? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1,60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('-=' * 3, f' SORTEANDO {quant} JOGOS ', '-=' * 3)
for i, l in enumerate(jogos):
    print(f'Jogo {i + 1}: {l}')
    sleep(1)
print('-=' * 5, '< BOA SORTE > ', '-=' * 5)
