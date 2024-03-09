"""
Faça um programa que tenha uma função chamada maior(),
que receba vários parâmetros com valores inteiros.

Seu programa tem que analisar todos os valores e dizer
qual deles é o maior.
"""
# from time import sleep
# def maior(* valores):
#     print('-' * 40)
#     print('Analisando os valores passados...')
#     for num in valores:
#         print(num, end=' ', flush=True)
#         sleep(0.5)

#     print(f'Foram informados {len(valores)} valores ao todo.')
#     maior = 0
#     for num in valores:
#         if num > maior:
#             maior = num
#     print(f'O maior valor informado foi {maior}.')

# maior(2,9,4,5,7,1)
# maior(4,7,0)
# maior(1,2)
# maior(6)
# maior()

# RESOLUÇÃO

from time import sleep
def maior(*num):
    cont = maior = 0
    print('-=' * 30)
    print('Analisando os valores passados...')
    for valor in num:
        print(f'{valor}', end=' ', flush=True)
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior =  valor
        cont+=1
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}')


# Programa principal
maior(2,9,4,5,7,1)
maior(4,7,0)
maior(1,2)
maior(6)
maior()