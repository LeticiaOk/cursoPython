"""
Crie um programa que tenha a função leiaint(), que
vai funcionar de forma semelhante à função input()
do Python. Só que fazendo a validação para aceitar
apenas um valor numérico.

Ex:
n = leiaint('Digite um n')
"""

# def leiaint(num):
#     while num.isnumeric() == False:
#         num = input('Digite um número: ')
#         if num.isnumeric() == False:
#             print('\033[31mERRO! Digite um número inteiro valido.\033[m')
#         else:
#             return num


# # Programa Principal
# n = leiaint('Digite um número: ')
# print(f'Você acabou de digitar o número {n}')

# RESOLUÇÃO
def leiaint(msg):
    ok =  False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[31mERRO! Digite um número interio válido\033[m')
        if ok:
            break
    return valor


# Programa principal
n = leiaint('Digite um número: ')
print(f'Você acabou de digitar o número {n}')