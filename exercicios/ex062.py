# primeiro = int(input('Primeiro termo: '))
# razao = int(input('Razão: '))
# pa = primeiro
# cont = 0
# termo = 9
# while cont <= 9:  
#     print(pa, end=' - ')
#     pa = pa + razao
#     cont += 1
# print('PAUSA')

# novaPa = pa - razao
# while termo != 0:
#     novocont = 0
#     termo = int(input('\nDeseja mostrar mais quantos termos? '))
#     while novocont <= termo - 1:
#         novaPa = novaPa + razao
#         print(novaPa, end=' - ')
#         novocont+=1
#         if novocont == termo:
#             print('PAUSA')
                
# print('Programa finalizado!')
 
print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print('{} - '.format(termo), end='')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão finalizada com {} termos mostrados'.format(total))