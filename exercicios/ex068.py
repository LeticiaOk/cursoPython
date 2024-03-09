from random import randint

print(21 * '-')
print('\033[31m JOGO DO PAR OU ÍMPAR\033[m')
print(21 * '-')

cont = 0
while True:
    
    computador = randint(1,10)

    jogador = int(input('Digite um valor de 1 a 10: '))
    opcao = str(input('Par ou ímpar? [P/I]: ')).upper().strip()
    
    soma = jogador + computador
    
    if soma % 2 == 0:
        resultado = 'PAR'
    else:
        resultado = 'ÍMPAR'
    print(50 * '-')
    print(f'Você jogou {jogador} e o computador {computador}. Total de {soma} DEU \033[33m{resultado}\033[m')
    print(50 * '-')
    if soma % 2 == 0 and opcao == 'P':
        print('\033[32mVOCÊ VENCEU!\033[m')
        cont += 1
        print('Vamos jogar novamente?')
        print(20 * '-')
        
    elif soma % 2 != 0 and opcao == 'I':
        print('\033[32mVOCÊ VENCEU!\033[m')
        cont += 1
        print('Vamos jogar novamente?')
        print(20 * '-')
    
    else:
        break

print('\033[31mVOCÊ PERDEU!\033[m')
print(12 * '-')
print(f'\033[33mGAME OVER!\033[m você venceu {cont} vezes')

# from random import randint
# v = 0
# while True:
#     jogador = int(input('Diga um valor: '))
#     computador = randint(0, 10)
#     total = jogador + computador
#     tipo = ' '
#     while tipo not in 'PI':
#         tipo = str(input('Par ou ímpar? [P/I] ')).strip().upper()[0]
#     print(f'Você jogou {jogador} e o computador {computador}. Total de {total} ', end='')
#     print('DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR')
#     if tipo == 'P':
#         if total % 2 == 0:
#             print('Você VENCEU!')
#             v += 1
#         else:
#             print('Você PERDEU!')
#             break
#     elif tipo == 'I':
#         if total % 2 == 1:
#             print('Você VENCEU!')
#             v += 1
#         else:
#             print('Você PERDEU!')
#             break
#     print('Vamos jogar novamente...')
# print(f'GAME OVER! Você venceu {v} vezes.')