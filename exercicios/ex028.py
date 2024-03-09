# import random 
# num = random.randint(0, 5)
# tentativa = int(input('Adivinhe o número escolhido entre 0 e 5: '))

# if tentativa == num:
#     print('Você venceu!')
# else:
#     print('Você perdeu.')
#     print('A resposta correta era o número {}.'.format(num))

from random import randint
from time import sleep
computador = randint(0, 5) # Faz o computador "PENSAR"
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei? ')) # O jogador tenta adivinhar
print('PROCESSANDO...')
sleep(3)
if jogador == computador:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('Ganhei! Eu pensei no número {} e não no {}'.format(computador, jogador))