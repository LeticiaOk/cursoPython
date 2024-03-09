# n = int(input('Digite um número para ver sua tabuada: '))

# for c in range(1, 11):
#     calculo = n * c
#     print('{} x {:2} = {}'.format(n, c, calculo))


num = int(input('Digite um número para ver sua tabuada: '))
for c in range(1, 11):
    print('{} x {:2} = {}'.format(num, c, num*c))