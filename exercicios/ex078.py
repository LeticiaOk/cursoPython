# valores = []
# for v in range(0,5):
#     valores.append(int(input(f'Digite um valor para a posição {v}: ')))

# print(f'Você digitou os valores {valores}')
# print(f'O maior valor digitado foi {max(valores)} nas posições: ', end='')

# maior = max(valores)

# for cont in range(0, len(valores)):
#     if valores[cont] == maior:
#         print(cont, end='...')

# menor = min(valores)

# print(f'\nO menor valor digitado foi {min(valores)} nas posições: ', end='')
# for cont in range (0, len(valores)):
#     if valores [cont] == menor:
#         print(f'{cont}', end='...')

#------------------------------------------------------------------------------

# for num in valores:
#     if num  == maior:
#         print(valores.index(num), end='...') #  método index() retorna a primeira ocorrência do valor no array. Portanto, quando você tem números repetidos, ele sempre encontrará a primeira ocorrência e imprimirá essa posição.

#------------------------------------------------------------------------------
# maior = max(valores)
# for indice, num in enumerate(valores):
#     if num == maior:
#         print(indice, end='...') # outra maneira


#RESOLUÇÃO

listanum = []
maior = 0
menor = 0

for c in range(0,5):
    listanum.append(int(input(f'Digite um valor para posição {c}: ')))
    if c == 0:
        maior = menor = listanum[c]
    else:
        if listanum[c] > maior:
            maior = listanum[c]
        if listanum[c] < menor:
            menor = listanum[c]

print('=-' * 30)
print(f'Você digitou os valores: {listanum}')
print(f'O maior valor digitado foi {maior} nas posições ', end='')
for i, v in enumerate(listanum):
    if v == maior:
        print(f'{i}...', end='')
print()
print(f'O menor valor digitado foi {menor} nas posições ', end='')
for i, v in enumerate(listanum):
    if v == menor:
        print(f'{i}...',end='')
print()