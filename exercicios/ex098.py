"""
Faça um programa que tenha uma função chamada
contador(), que receba três parâmetros: inicio, fim
e passo e realize a contagem.

Seu programa tem que realizar três contagens atravês
da função criada:

a) De 1 até 10, de 1 em 1
b) De 10 até 0, de 2 em 2
c) Uma contagem personalizada
"""

# from time import sleep
# def contador(i,f,p):
#     if p < 0:
#         p *= -1
#     if p == 0:
#         p =1
#     print('-' * 30)
#     print(f'Contagem de {i} até {f} de {abs(p)} em {abs(p)}')
    
#     if i < f and p > 0 :
#         for c in range(i,f+p,p):
#             print(c, end=' ', flush=True)
#             sleep(0.3)
#         print('FIM!')
#     elif i > f and p > 0:
#         for c in range(i,f-p,-p):
#             if c >= f:
#                 print(c, end=' ', flush=True)
#                 sleep(0.3)
#         print('FIM!')

# contador(1,10,1)
# contador(10,0,2)
# print('-' * 30)
# print('Agora é sua vez de personalizar a contagem!')
# contador(int(input('Início: ')), int(input('Fim: ')), int(input('Passo: ')))

# RESOLUÇÃO

from time import sleep
def contador(i,f,p):
    if p < 0:
        p*= -1
    if p == 0:
        p = 1
    print('-=' * 20)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    sleep(2.5)
   
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont}', end=' ', flush=True)
            sleep(0.3)
            cont+=p
        print('FIM!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont}', end=' ', flush=True)
            sleep(0.3)
            cont-=p
        print('FIM!')

# Programa principal
contador(1,10,1)
contador(10,0,2)
print('-=' * 20)
print('Agora é sua vez de personalizar a contagem!')
ini = int(input('Início: '))
fim = int(input('Fim:    '))
pas = int(input('Passo:  '))
contador(ini,fim,pas)