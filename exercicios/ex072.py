# contagem = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

# numero = int(input('Digite um número: '))
# print(f'Você digitou o número \033[31m{contagem[numero].upper()}\033[m')

cont = ('zero', 'um', 'dois', 'três', 'quatro',
       'cinco', 'seis', 'sete', 'oito', 'nove',
       'dez', 'onze', 'doze', 'treze', 'quatorze',
       'quinze', 'dezesseis', 'dezessete', 'dezoito',
       'dezenove', 'vinte')

# while True:
#     num = int(input('Digite um número entre 0 e 20: '))
#     if 0 <= num <= 20: # Se o número estiver entre 0 e 20
#         break
#     print('Tente novamente. ', end='')
# print(f'Você digitou o número {cont[num]}')

resp = 'S'
while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if 0 <= num <= 20: # Se o número estiver entre 0 e 20
       print(f'Você digitou o número {cont[num]}')

      
       while resp == 'S':
        resp = ('Deseja continuar [S/N]?')

        num = int(input('Digite um número entre 0 e 20: '))
        print(f'Você digitou o número {cont[num]}')

    else:
            print('Tente novamente. ', end='')

#     print('Tente novamente. ', end='')
# print(f'Você digitou o número {cont[num]}')