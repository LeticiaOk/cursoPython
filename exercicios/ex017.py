# import math
# co = int(input('Digite o comprimento do cateto oposto do triâgulo retangulo: '))
# ca = int(input('Digite o comprimento d cateto adjacente do triângulo retangulo: '))
# calculo = math.sqrt((math.pow(co, 2) + math.pow(ca, 2)))
# print('O comprimento da hipotenusa é: {}'.format(calculo))

# co = float(input('Comprimento do cateto oposto: '))
# ca  = float(input('Comprimento do cateto adjacente: '))
# hi = (co ** 2 + ca **2) ** (1/2)
# print('A hipotenusa vai medir {:.2f}'.format(hi))

from math import hypot
co = float(input('Comprimento do cateto oposto: '))
ca  = float(input('Comprimento do cateto adjacente: '))
hi = hypot(co, ca)
print('A hipotenusa vai medir: {:.2f}'.format(hi))