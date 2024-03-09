"""
Crie um programa que tenha uma função fatorial() que
recebra dois parâmetros: o primeiro que indique o 
número a calcular e o outro chamado show, que será um
valor lógico (opcional) indicando se será mostrado ou
não na tela o processo de cálculo do fatorial.
"""


# def fatorial(num, show=False):
#     produto = 1
#     for c in range(num, 0, -1):
#         produto*=c
#         if show == True:
#             if c > 1:
#                 print(f'{c} x ',end='')
#             else:
#                 print(f'{c} = ', end='')            
#     return produto


# # programa principal
# print(fatorial(5))

# RESOLUÇÃO
def fatorial(n, show=False):
    """
    -> Calcula o Fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do Fatorial de um número n
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(f' x ',end='')
            else:
                print(' = ', end='')
        f *= c
    return f

#Programa principal
print(fatorial(5))