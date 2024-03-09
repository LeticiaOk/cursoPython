from random import choice
from time import sleep
print(15*'-')
print('\033[32mjOGO DO JOKENPÔ\033[m')
print(15*'-')

pedra = 'pedra'
papel = 'papel'
tesoura = 'tesoura'

opcao = [pedra, papel, tesoura]

computador = choice(opcao)
usuario = input('Escolha pedra, papel ou tesoura: ')
print('\033[31mJOKENPÔ!\033[m')
sleep(1)

if computador == 'pedra' and usuario == 'tesoura':
    print('\033[34mRESULTADO:\033[m')
    print('\033[33mcomputador: Pedra\033[m')
    print('\033[33mUsuário: Tesoura\033[m')
    print('\033[34mVenci! pedra ganha tesoura.\033[m')
elif computador == 'papel' and usuario == 'pedra':
    print('\033[34mRESULTADO:\033[m')
    print('\033[33mcomputador: papel.\033[m')
    print('\033[33mUsuário: pedra\033[m')
    print('\033[34mVenci! papel ganha pedra.\033[m')
elif computador == 'tesoura' and usuario == 'papel':
    print('\033[34mRESULTADO:\033[m')
    print('\033[33mcomputador: tesoura\033[m')
    print('\033[33mUsuário: papel\033[m')
    print('\033[34mVenci! tesoura ganha papel.\033[m')


elif computador == 'tesoura' and usuario == 'pedra':
    print('\033[34mRESULTADO:\033[m')
    print('\033[33mComputador: tesoura\033[m')
    print('\033[33mUsuário: pedra\033[m')
    print('\033[34mVocê venceu! pedra ganha tesoura.\033[m')
elif computador == 'pedra' and usuario == 'papel':
    print('\033[3m4RESULTADO:\033[m')
    print('\033[33mComputador: pedra\033[m')
    print('\033[33mUsuário: papel\033[m')
    print('\033[34mVocê venceu! papel ganha pedra.\033[m')
elif computador == 'papel' and usuario == 'tesoura':
    print('\033[34mRESULTADO:\033[m')
    print('\033[33mComputador: papel\033[m')
    print('\033[33mUsuário: tesoura\033[m')
    print('\033[34mVocê venceu! tesoura ganha papel.\033[m')

elif computador == 'tesoura' and usuario == 'tesoura':
    print('\033[34mRESULTADO:\033[m')
    print('\033[33mComputador: tesoura\033[m')
    print('\033[33mUsuário: tesoura\033[m')
    print('\033[34mEmpate!\033[m')

elif computador == 'pedra' and usuario == 'pedra':
    print('\033[34mRESULTADO:\033[m')
    print('\033[33mComputador: pedra\033[m')
    print('\033[33mUsuário: pedra\033[m')
    print('\033[34mEmpate!\033[m')

elif computador == 'papel' and usuario == 'papel':
    print('\033[34mRESULTADO:\033[m')
    print('\033[33mComputador: papel\033[m')
    print('\033[33mUsuário: papel\033[m')
    print('\033[34mEmpate!\033[m')

# from random import randint
# from time import sleep
# itens = ('Pedra', 'Papel', 'Tesoura')
# computador = randint(0, 2)
# print('O compuadro escolheu {}'.format(itens[computador]))
# print('''SUAS OPÇÕES:
# [0] PEDRA
# [1] PAPEL
# [2] TESOURA''')
# jogador = int(input('Qual é a sua jogada? '))
# print('JO')
# sleep(1)
# print('KEN')
# sleep(1)
# print('PO!!')
# print('-=' * 11)
# print('Computador jogou {}'.format(itens[computador]))
# print('Jogador jogou {}'.format(itens[jogador]))
# print('-=' * 11)

# if computador == 0: # compuador jogou pedra
#     if jogador == 0:
#         print('EMPATE')
#     elif jogador == 1:
#         print('JOGADOR VENCE')
#     elif jogador == 2:
#         print('COMPUTADOR VENCE')
#     else:
#         print('JOGADA INVÁLIDA!')
# elif computador == 1:# compuador jogou papel
#     if jogador == 0:
#         print('COMPUTADOR VENCE')
#     elif jogador == 1:
#         print('EMPATE')
#     elif jogador == 2:
#         print('JOGADOR VENCE')
#     else:
#         print('JOGADA INVÁLIDA!')
# elif computador == 2: # compuador jogou tesoura
#     if jogador == 0:
#         print('JOGADOR VENCE')
#     elif jogador == 1:
#         print('COMPUTADOR VENCE')
#     elif jogador == 2:
#         print('EMPATE')
#     else:
#         print('JOGADA INVÁLIDA!')