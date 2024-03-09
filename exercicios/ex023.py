# numero = input('Digite um número de 0 a 9999: ')
# print('Unidade: {}'.format(numero[-1]))
# print('Dezena: {}'.format(numero[-2]))
# print('Centena: {}'.format(numero[-3]))
# print('Milhar: {}'.format(numero[-4]))

num = int(input('Informe um número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analisando o número: {}'.format(num))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))