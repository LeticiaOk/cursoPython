"""
Reescreva a função leiaInt() que fizemos no desafio 
104, incluindo a gora a possibilidade da digitação de
um número de tipo inválido.
Aproveite e crie também uma função leiaFloat() com a
mesma funcionalidade
"""

# def leiaInt(msg):
#     while True:
#         try:
#             ni = int(input(msg))
#         except ValueError:
#             print('\033[31mERRO: por favor, digite um número inteiro válido.\033[m')
#         except KeyboardInterrupt:
#             print('\033[31m\nUsuário preferiu não digitar esse número.\033[m')
#             return 0       
#         else:
#             return ni

# def leiaFloat(msg):
#     while True:
#         try:
#             nr = float(input(msg))
#         except ValueError:
#             print('\033[31mERRO! por favor, digite um número real válido.\033[m')
#         except KeyboardInterrupt:
#             print('\033[31m\nO usuário preferiu não digititar esse número\033[m')
#             return 0
#         else:
#             return nr
        
# # Programa principal
# ni = leiaInt('Número Inteiro: ')
# nr = leiaFloat('Número Real: ')
# print(f'O valor inteiro digitado foi {ni} e o real foi {nr}')

# RESOLUÇÃO
def leiaInt(msg):
    while True:
        try:
            n  =int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: Por favor, digite um número inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print(f'\n\033[31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n

def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um número real válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n
        
n1 = leiaInt('Digite um  Inteiro: ')
n2 = leiaFloat('Digite um Real: ')
print(f'O valor inteiro digitado foi {n1} e o real foi {n2}')