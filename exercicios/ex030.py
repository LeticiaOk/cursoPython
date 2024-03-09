# num = int(input('Digite um número inteiro : '))

# if num % 2 == 0:
#     print('Número par')
# else:
#     print('Número impar')

numero =int(input('Me diga um número qualquer: '))
resultado = numero % 2
if resultado == 0:
    print('O número {} é PAR'.format(numero))
else:
    print('O número {} é ÍMPAR'.format(numero))