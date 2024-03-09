
#LISTAS

# lanche = ['cachorro-quente', 'hamburguer', 'suco', 'pizza', 'picolé', 'cookie']

# #Adicionar elementos na lista
# lanche.append('cookie') # adiciona um elemento no final da lista
# lanche.insert(0,'pizza') # adiciona um elemento em qualquer posição da lista (os índices dos elementos muda)

# #Eliminar elementos da lista
# del lanche[3] # remove o elemento 3 da lista
# lanche.pop(3) # geralmente usado para remover o último elemento da lsia
# lanche.pop() # remove o último elemento da lista
# lanche.remove('pizza') # indica o valor que quer remover ao invés do índice
# #reposiciona a contagem dos índices

# #Remover itens que não estão na lista
# if 'pizza' in lanche:
#     lanche.remove('pizza')

# #Criar listas através de range
# valores = list(range(4,11)) # Faz uma contagem de 4 a 10 e coloca dentro de uma lista de 0 a 6
# valores = list(range(4,11, 2)) # Faz uma contagem de 4 a 10 pulando de 2 em 

# #Colocar elementos em ordem
# valores[8,2,5,4,9,3,0]
# valores.sort() # Ordena os valores em ordem crescente
# valores.sort(reverse=True) # Deixa os elementos em ordem decrescente

#AULA PRÁTICA
# num = [2,5,9,1,]
# num[2] = 3 #muda o indice 2 (9) para 3
# num[4] = 7 # não da para dicionar no indice 4 porque só tem 3 indices
# num.insert(2,0) #na posição 2 adiciona o 0

# LAÇO
# num = [2,5,9,1,]

# num.insert(2,2)
# if 5 in num:
#     num.remove(5) # removeu o numero 5
# else:
#     print('Não achei o número 5')

# REMOVER
# num = [2,5,9,1]
# num[2] = 3 #muda o indice 2 (9) para 3
# num.append(7) # adiciona o 7 no final do elemento (no indice 4 no caso)
# num.sort(reverse=True) # o 7 esta na posição 0 por conta do reverse
# num.pop(2) # remove o indice da segunda posição com base na reverse ou seja o indice 2 porém se vier antes do reverse eleimina o indice com base na lista original
# print(num)

#ORDEM DE APARIÇÃO
# num = [2,5,9,1]
# num[2] = 3 #muda o indice 2 (9) para 3
# num.sort(reverse=True) # p 7 esta na posição 0 por conta do reverse
# num.append(7) # adiciona o 7 no final do elemento (no indice 4 no caso)
# num.insert(2,2)
# num.remove(2) # só elimina o primeiro elemento 2
# print(num)


#MOSTRANDO VALORES
# valores = list() # lista vazia com parênteses
# valores = []
# valores.append(5)
# valores.append(9) # adiciona valores a lista
# valores.append(4)

# for v in valores:
#     print(f'{v}...', end='')
# print(valores) # printa os valores na tela formatados


# for c, v in enumerate(valores):
#     print(f'Na posição {c} encontrei o valor {v}!')
# print('Cheguei ao final da lista') #mostra as chaves e os valores


# valores = []
# for cont in range(0, 5):
#     valores.append(int(input('Digite um valor: '))) # adiciona valores com o append


# a = [2, 3, 4, 7]
# b = a 
# b[2] = 8 # vai mudar os valores das duas listas para 8 :O
# print(f'lista A: {a}')
# print(f'lista B: {b}')

# a = [2, 3, 4, 7]
# b = a[:] # b recebe todos os itens de a porém como cópia
# b[2] = 8 # apenas a lista b irá ser alterada
# print(f'lista A: {a}')
# print(f'lista B: {b}')
