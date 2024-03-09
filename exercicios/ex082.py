valores = []
pares = []
impares = []

while True:
    valores.append(int(input('Digite um valor: ')))
    
    resp = input('Deseja continuar? [S/N]: ').upper()

    while resp != 'N' and resp !='S':
        resp = input('Opção inválida, apenas [S] para SIM ou [N] para NÃO: ').upper()

    if resp == 'N':
        break

for num in valores:
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)
print('-' * 40)
print(f'Lista completa: {valores}')
print(f'Lista de pares: {pares}')
print(f'Lista de impares: {impares}')

    # for v in valores:
#     print(f'{v}...', end='')
# print(valores) # printa os valores na tela formatados


# for c, v in enumerate(valores):
#     print(f'Na posição {c} encontrei o valor {v}!')
# print('Cheguei ao final da lista') #mostra as chaves e os valores