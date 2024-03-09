# total = 0
# mil = 0
# cont = 0
# while True:

#     opcao = ''

#     nome = str(input('Digite o nome do produto: '))
#     preco = float(input('Digite o preço do produto: R$'))
    
#     cont += 1
#     total += preco

#     if preco > 1000:
#         mil+= 1

#     if cont == 1:
#         barato = preco
#         baratonome = nome
#     else:
#         if preco < barato:
#             barato = preco
#             baratonome = nome

#     while opcao != 'N' and opcao != 'S':
#         opcao = str(input('Deseja continuar [S/N]? ')).upper().strip()
    
#     if opcao == 'N':
#         break

# print('-' * 40)
# print(f'Total gasto na compra: R${total:.2f}')
# print(f'Total de produtos acima de \033[31mR$1000.00\033[m: {mil}')
# print(f'Produto mais barato: {baratonome}')
# print('-' * 40)

total = totmil = menor = cont = barato = 0
while True:
    produto = str(input('Nome do prduto: '))
    preco = float(input('Preco: R$'))
    cont += 1
    total += preco
    if preco > 1000:
        totmil += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('{:-^40}'.format(' FIM DO PROGRAMA '))
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {totmil} produtos custando mais de R$1000.00')
print(f'O produtos mais barato foi{barato} que custa R${menor:.2f}')