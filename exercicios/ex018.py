# import math
# angulo = int(input('Digite o ângulo: '))
# seno = ...
# cosseno = ...
# tangente = ...

# print('O seno da circunferência é: {}'.format(seno))
# print('O cosse da circunferência é: {}'.format(cosseno))
# print('A tangente é: {}'.format(tangente))

# import math
# angulo = float(input('Digite o ângulo que você deseja: '))

# seno = math.sin(math.radians(angulo))
# print('O ângulo de {} tem o SENO de {:.2f}'.format(angulo,seno))

# cosseno = math.cos(math.radians(angulo))
# print('O ângulo de {} tem o COSSENO de {:.2f}'.format(angulo, cosseno))

# tangente = math.tan(math.radians(angulo))
# print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(angulo, tangente))

from math import radians, sin, cos, tan
angulo = float(input('Digite o ângulo que você deseja: '))

seno = sin(radians(angulo))
print('O ângulo de {} tem o SENO de {:.2f}'.format(angulo,seno))

cosseno = cos(radians(angulo))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(angulo, cosseno))

tangente = tan(radians(angulo))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(angulo, tangente))