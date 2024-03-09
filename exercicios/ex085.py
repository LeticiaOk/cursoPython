# valores = [[],[]]
# num = 0
# for c in range(1, 8):
#     num = int(input(f'Digite o {c}º valor: '))

#     if num % 2 == 0:
#       valores[0].append(num)
#     else:
#       valores[1].append(num)

# valores[0].sort()
# valores[1].sort()
# print(f'Os valores pares digitados foram: {valores[0]}')
# print(f'Os valores ímpares digitados foram: {valores[1]}')

# RESOLUÇÃO

num = [[],[]]
valor = 0
for c in range(1, 8):
    valor = int(input(f'Digite o {c}º valor: '))
    if valor % 2 == 0:
      num[0].append(valor)
    else:
       num[1].append(valor)
print('-=' * 30)
num[0].sort()
num[1].sort()
print(f'Os valores pares digitados foram: {num[0]}')
print(f'Os valores ímpares digitados foram: {num[1]}')
    
