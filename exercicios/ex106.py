"""
Faça um mini-sistema que utilize o interactive help
do Python. O usuário vai digitar o comando e o
manual vai aparecer. Quando o usuário digitar a
palavra 'FIM', o programa se encerrará.

OBS: use cores.
"""
# MENSAGENS
#----------------------------------------------------------
# def titulo():
#     titulo = 'SISTEMA DE AJUDA PyHELP'
#     print('\033[34m')
#     print('-' * len(titulo))
#     print(titulo)
#     print('-' * len(titulo))
#     print('\033[m')
# #--------------------------------------------------------
# def acesso():
#     acesso = f'Acessando o manual do comando {comando}'
#     print('\033[33m')
#     print('-' * len(acesso))
#     print(acesso)
#     print('-' * len(acesso))
#     print('\033[m')

# #---------------------------------------------------------
# def fim():
#     fim = 'ATÉ LOGO!'
#     print('\033[31m')
#     print('-' * len(fim))
#     print(fim)
#     print('-' * len(fim))
#     print('\033[m')
# #----------------------------------------------------------

# # MANUAL
# def manual():  
    
#     chave=''
#     while chave != 'fim':
#         titulo()
#         chave = input('Função ou Biblioteca > ')
#         if chave =='fim':
#             break
#         global comando
#         comando = chave
#         acesso()
#         print('\033[32m')
#         help(chave)
#         print('\033[m')
#     fim()

# # programa principal
# manual()

# RESOLUÇÃO
from time import sleep


c = ('\033[m',          # 0 - sem cores
     '\033[0;30;41m',   # 1 - vermelho
     '\033[0;30;42m',   # 2 -verde
     '\033[0;30;43m',   # 3 - amarelo
     '\033[0;30;44m',   # 4- azul
     '\033[0;30;45m',   # 5 - roxo
     '\033[7;30m'       # 6 - branco
     );


def ajuda(com):
    titulo(f'Acessando o manual do comando \'{com}\'', 4)
    print(c[6], end='')
    help(com)
    print(c[0], end='')
    sleep(2)



def titulo(msg,cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f'  {msg}  ')
    print('~' * tam)
    print(c[0], end='')
    sleep(1)

# Programa principal
comando = ''
while True:
    titulo('SISTEMA DE AJUDA PYHELP',2)
    comando = str(input("Função ou Biblioteca > "))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('ATÉ LOGO',3)





