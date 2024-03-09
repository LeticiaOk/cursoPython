# listagem = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00, 'Tranferidor', 4.20, 'Compasso',9.99,'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)

# print(f'{listagem[0]}...................R$ {listagem[1]}')
# print(f'{listagem[2]}................R$ {listagem[3]:.2f}')
# print(f'{listagem[4]}.................R$ {listagem[5]:.2f}')
# print(f'{listagem[6]}..................R$ {listagem[7]:.2f}')
# print(f'{listagem[8]}.............R$ {listagem[9]:.2f}')
# print(f'{listagem[10]}................R$ {listagem[11]}')
# print(f'{listagem[12]}.................R$ {listagem[13]:.2f}')
# print(f'{listagem[14]}.................R$ {listagem[15]:.2f}')
# print(f'{listagem[16]}...................R$ {listagem[17]:.2f}')

listagem = ('Lápis', 1.75,
            'Borracha', 2.00,
            'Caderno', 15.90,
            'Estojo', 25.00,
            'Tranferidor', 4.20,
            'Compasso',9.99,
            'Mochila', 120.32,
            'Canetas', 22.30,
            'Livro', 34.90)

# for item in listagem:
#     if item % 2 == 0:
#         print(f'{listagem[item]:.<30}',end='')
#     else:
#         print(f'R${listagem[item]:>7.2f}') # : Quando você faz for item in listagem:, item recebe os valores da tupla ('Lápis', 1.75, 'Borracha', ...) e não os índices. Portanto, você não pode usar item como um índice para acessar elementos da tupla.

print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' * 40)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}',end='')
    else:
        print(f'R${listagem[pos]:>7.2f}')
print('-' * 40)
