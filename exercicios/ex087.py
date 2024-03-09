# dado = 0
# matriz = [[], [], [], [], [], [], [], [],[]]
# m1 = 0
# m2 = 0
# tot_m1 = 0
# for cont in range(len(matriz)):
#     dado = int(input(f'Digite um valor para [{m1}, {m2}]: '))
#     tot_m1 += 1
#     m2+=1

#     if tot_m1 == 3:
#         m1+=1
#         tot_m1 = 0

#     if m2 == 3:
#         m2 = 0

#     matriz[cont].append(dado)

# tot_cont = 0 
# for cont in range(len(matriz)):
#     print(matriz[cont],end='')
#     tot_cont+=1
#     if tot_cont == 3:
#         tot_cont = 0
#         print('\n', end='')

# soma_par = 0
# soma_coluna = 0
# for cont in range(len(matriz)):
#     if matriz[cont][0] % 2 == 0:
#         soma_par+=matriz[cont][0]

# soma_coluna = 0
# tot_cont_coluna = 0
# for cont in range(len(matriz)):
#    tot_cont_coluna+=1
#    if tot_cont_coluna == 3 or tot_cont_coluna == 6 or tot_cont_coluna == 9:
#        soma_coluna+=matriz[cont][0]

# tot_linha = 0
# maior = 0
# for cont in range(len(matriz)):
#     tot_linha+=1
#     if tot_linha == 4 and matriz[cont][0] > maior:
#         maior = matriz[cont][0]
#     elif tot_linha == 5 and matriz[cont][0] > maior:
#         maior = matriz[cont][0]
#     elif tot_linha == 6 and matriz[cont][0] > maior:
#         maior = matriz[cont][0]

        
# print(f'soma dos valores pares: {soma_par}')
# print(f'Soma dos valores da terceira coluna: {soma_coluna}')
# print(f'Maior valor da segunda linha: {maior}')

# RESOLUÇÃO

matriz = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]
spar = mai = scol = 0
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('-=' * 30)
for l in range(0, 3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]',end='')
        if matriz[l][c] % 2 == 0:
            spar += matriz[l][c]
    print()
print('-=' * 30)
print(f'A soma dos valores pares é {spar}')
for l in range(0, 3):
    scol += matriz[l][2]
print(f'A soma dos valores da terceira coluna é {scol}')
for c in range(0, 3):
    if c == 0:
        mai = matriz[1][c]
    elif matriz[1][c] > mai:
        mai = matriz[1][c]
print(f'O maior valor da segunda linha é {mai}')