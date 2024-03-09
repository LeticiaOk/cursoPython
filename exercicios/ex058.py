# from random import randint
# from time import sleep

# palpite= 1
# computador = randint(0, 10) # Faz o computador "PENSAR"
# print('-=-' * 20)
# print('Vou pensar em um número entre 0 e 10. Tente adivinhar...')
# print('-=-' * 20)
# jogador = int(input('Em que número eu pensei? ')) # O jogador tenta adivinhar
# print('PROCESSANDO...')
# sleep(3)


# while jogador != computador:
#    jogador = int(input('Ops... você errou! tente novamente: '))
#    palpite += 1
# print('PARABÉNS! Você conseguiu me vencer, o número era: {}!'.format(computador))
# print('Número de palpites: {}'.format(palpite))

from random import randint
computador = randint(0, 10)
print('Sou seu computador acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi? ')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
      if jogador < computador:
            print('Mais... Tente mais uma vez.')
      elif jogador > computador:
            print('Menos... Tente mais uma vez.')
print('Acertou com {} tentativas. Parabéns!'.format(palpites))
