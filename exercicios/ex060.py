
# num = int(input('Digite um número para ver seu fatorial: '))
# print('{}! = {}'.format(num, num), end='')

# cont = num - 1
# multiplicacao = num
# while cont > 0:
#     print( ' x ',cont, end='')
#     multiplicacao = multiplicacao * cont
#     cont-= 1
   
# print(' = ',multiplicacao)

# from math import factorial
# n = int(input('Digite um número para calcular seu Fatorial: '))
# f = factorial(n)
# print('O fatorial de {} é {}'.format(n, f))

n = int(input('Digite um número para calcular seu Fatorial: '))
c = n
f = 1
print('Calculando {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ',end='')
    f *= c
    c -= 1


print('{}'.format(f))
