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
#     print(f'{matriz[cont]:^5}',end='')
#     tot_cont+=1
#     if tot_cont == 3:
#         tot_cont = 0
#         print('\n', end='')


# RESOLUÇÃO

matriz = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('-=' * 30)
for l in range(0, 3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]',end='')
    print()