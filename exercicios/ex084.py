"""Faça um programa que leia o nome e peso de várias pessoas
guardando tudo em uma lista. No final mostre:

A) Quantas pessoas foram cadastradas.

B) Uma listagem com as pessoas mais pesadas.

C) Uma listagem com pessoas leves."""

pessoas = []
dados = []
maipeso_lista_nome = []
maipeso_lista = []
menpeso_lista = []
menpeso_lista_nome = []
continuar = 'S'
total = 0
maipeso = 0
maipeso_nome = ''
menpeso = 0
menpeso_nome = ''

while continuar == 'S':
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Peso: ')))
    pessoas.append(dados[:])
    total+=1

    if dados[1] >= maipeso:
        maipeso = dados[1]
        maipeso_nome = dados[0]
        maipeso_lista_nome.append(maipeso_nome)
        maipeso_lista.append(maipeso)

   
    if total == 1:
        menpeso = dados[1]
        menpeso_nome = dados[0]
        menpeso_lista_nome.append(menpeso_nome)
        menpeso_lista.append(menpeso)
    else:
        if dados[1] <= menpeso:
            menpeso = dados[1]
            menpeso_nome = dados[0]
            menpeso_lista_nome.append(menpeso_nome)
            menpeso_lista.append(menpeso)
    
    for i in maipeso_lista:
        if i < maipeso:
            maipeso_lista.pop(0)
            maipeso_lista_nome.pop(0)
    
    for i in menpeso_lista:
        if i > menpeso:
            menpeso_lista.pop(0)
            menpeso_lista_nome.pop(0)
        
    
    dados.clear() 

    continuar = input('Deseja continuar? [S/N] ').upper()


print(f'O maior peso foi de {maipeso}. Peso de {maipeso_lista_nome}')
print(f'O menor peso foi de {menpeso}. Peso de {menpeso_lista_nome}')





# pessoas = []
# dados = []
# maipeso_lista_nome = []
# menpeso_lista_nome = []
# lista_peso = []
# lista_nome = []
# continuar = 'S'
# total = 0
# maipeso = 0
# menpeso = 0

# while continuar == 'S':
#     dados.append(str(input('Nome: ')))
#     dados.append(float(input('Peso: ')))
#     pessoas.append(dados[:])
#     lista_nome.append(dados[0])
#     lista_peso.append(dados[1])
#     total+=1

#     if dados[1] >= maipeso:
#         maipeso = dados[1]
   
#     if total == 1:
#         menpeso = dados[1]

#     else:
#         if dados[1] <= menpeso:
#             menpeso = dados[1]

#     dados.clear() 

#     continuar = input('Deseja continuar? [S/N] ').upper()

# for cont in range(0, len(lista_peso)):
#     if lista_peso[cont] == maipeso:
#         maipeso_lista_nome.append(lista_nome[cont])

# for cont in range(0,len(lista_peso)):
#     if lista_peso[cont] == menpeso:
#         menpeso_lista_nome.append(lista_nome[cont])

# print(f'Ao todo foram cadastradas {total} pessoas')
# print(f'O maior peso foi de {maipeso}. Peso de {maipeso_lista_nome}')
# print(f'O menor peso foi de {menpeso}. Peso de {menpeso_lista_nome}')


#RESOLUÇÃO

# temp = []
# princ = []
# mai = men = 0

# while True:
#     temp.append(str(input('Nome: ')))
#     temp.append(float(input('Peso: ')))
#     if len(princ) == 0:
#         mai = men = temp[1]
#     else:
#         if temp[1] > mai:
#             mai = temp[1]
#         if temp[1] < men:
#             men = temp[1]
#     princ.append(temp[:])
#     temp.clear()
#     resp = str(input('Quer continuar? [S/N] '))
#     if resp in 'Nn':
#         break

# print('-=-' * 30)
# # print(f'Os dados foram {princ}')
# print(f'Ao todo você cadastrou {len(princ)} pessoas.')
# print(f'O maior peso foi de {mai}Kg. Peso de ', end='')
# for p in princ:
#     if p[1] == mai:
#         print(f'[{p[0]}] ', end='')
# print()
# print(f'O menor peso foi de {men}Kg. Peso de ', end='')
# for p in princ:
#     if p[1] == men:
#         print(f'[{p[0]}] ',end='')
# print()