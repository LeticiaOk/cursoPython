# num1 = int(input('Digite o primeiro número: '))
# num2 = int(input('Digite o segundo número: '))
# num3 = int(input('Digite o terceiro número: '))

# if num1 > num2 and num1 > num3:
#     print('O maior número é {}'.format(num1))
# elif num2 > num1 and num2 > num3:
#     print('O maior número é {}'.format(num2))
# else:
#     print('O maior número é {}'.format(num3))

# if num1 < num2 and num1 < num3:
#     print('O menor número é: {}'.format(num1))
# elif num2 < num1  and num2 < num3:
#     print('O menor número é: {}'.format(num2))
# else:
#     print('O menor número é: {}'.format(num3))

a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))
# Verificando quem é o menor
menor = a
if b < a and b < c:
    menor = b
if c<a and c<b:
    menor = c
# Verificando quem é o maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O menor valor digitado foi {}'.format(menor))
print('O maior valor digitado foi {}'.format(maior))
