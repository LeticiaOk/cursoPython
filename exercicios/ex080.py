
# valores = []

# for v in range(0, 5):
#     num = int(input('Digite um valor: '))
    
#     if v == 0:
#         valores.append(num)
#         menor = num
#         maior = num
#     else:
#         if num <= menor:
#             valores.insert(0, num)
#             menor = num
#         elif num >= maior:
#             valores.append(num)
#             maior = num
#         else:
#             for i in range(len(valores)):
#                 if valores[i] >= num:
#                     valores.insert(i, num)
#                     break
# print(valores)

#RESULUÇÃO
lista = []

for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print('Adicionado ao final da lista')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionado da posição {pos} da lista')
                break
            pos+= 1
print('-=' * 30)
print(f'Os valores digitados em ordem foram {lista}')
