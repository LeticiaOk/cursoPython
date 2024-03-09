# from random import randint

# valores = ()
# for c in range(0,5):
#     num = randint(0,10)
#     valores = valores + (num,)

#     if c == 0:
#         maior = num
#         menor = num
#     else:
#         if num > maior:
#             maior = num
#         if num < menor:
#             menor = num
# print(valores)
# print(f'Maior valor {maior}')
# print(f'Menor valor: {menor}')

from random import randint

numeros = (randint(1,10), randint(1,10) ,randint(1,10), randint(1,10), randint(1,10))
print('Os valores sorteados foram: ', end='')
for n in numeros:
    print(f'{n}', end=' ')
print(f'\nO maior valor sorteado foi {max(numeros)}')
print(f'O menor valor sorteado foi {min(numeros)}')
