"""
Fsça um programa que tenha uma função chada área(),
que receba as dimensões de um terreno retangular
(largura e comprimento) e mostra a área do terreno
"""

# def mensagem(msg):
#     print(msg)
#     print('-'*30)

# mensagem('\nControle de Terrenos')

# def area(l,a):
#     produto = l*a
#     print(f'A área de um terreno {l} x {a} é de {produto:.1f}².')

# # Programa principal
# area(float(input('LARGURA (m): ')), float(input('COMPRIMENTO (m): ')))

# RESOLUÇÃO

def area(larg,comp):
    a = larg * comp
    print(f'A área de um terreno {larg}x{comp} é de {a}m² ')

# Programa principal
print('Controle de Terrenos')
print('-' * 20)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
area(l,c)