# num = 0
# soma = 0
# cont = 0
# while num != 999:
#     num = int(input('Digite um número: '))
#     soma += num
#     cont += 1
# print('Total de números: {}'.format(cont - 1))
# print('Total da soma: {} '.format(soma - 999))

num = cont = soma = 0
num = int(input('Digite um número [999 para parar]: '))

while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite um número [999 para parar]: '))
print('Você digitou {} números e a soma entre eles foi {}. '.format(cont, soma))
