"""
Faça um programa que tenha uma função chamada
escreva(), que receba um texto qualquer como parâmetro
e mostre uma mensagem com tamanho adaptável.

Ex: 
escreva('Olá, mundo!')

Saída:
-----------
Olá, Mundo!
-----------
"""

# def escreva(txt):
#     cont = 0
#     print('-' * len(txt))
#     print(txt)
#     print('-' * len(txt))
 

# # programa principal
# escreva('Gustavo Guanabara')
# escreva('Curso de Python no YouTube')
# escreva('CeV')
# escreva(str(input('Escreva algo: ')))

# RESOLUÇÃO
def escreva(msg):
    tam = len(msg) + 4
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)

# Programa principal
escreva('Gustavo Guanabara')
escreva('Curso de Python no Youtube')
escreva('Cev')