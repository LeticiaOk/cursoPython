"""
Faça um programa que tenha uma lista chamada números
e duas funções chamadas sorteio() e somapar().
A primeira função vai sortear 5 números e colocá-los
dentro de uma lista e a segunda função vai mostrar a 
soma entre todos os valores PARES soteados pela
função anterior.
"""
# from random import randint
# from time import sleep
# numeros = []
# def sorteio():
#     print('Soteando 5 valores da lista: ',end='')
#     for c in range(0,5):
#         numeros.append(randint(1,10))
#         print(numeros[c],end=' ', flush=True)
#         sleep(1)
# sorteio()

# def somapar():
#     soma = 0
#     for num in numeros:
#         if num % 2 == 0:
#             soma+=num
#     print(f'\nSomando os valores pares de {numeros}, temos {soma}')
# somapar()

# RESOLUÇÃO
from random import randint
from time import sleep
def sorteia(lista):
    print('Soteando 5 valores da lista: ', end='')
    for contador in range(0,5):
        n = randint(1,10)
        lista.append(n)
        print(f'{n}', end=' ', flush=True)
        sleep(0.3)
    print('PRONTO!')


def somapar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma+=valor
    print(f'Somando os valores pares de {lista}, temos {soma}')
        


numeros = list()
sorteia(numeros)
somapar(numeros)