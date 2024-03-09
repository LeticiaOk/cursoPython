#TUPLAS

# lanche = ('hamburger', 'suco', 'pizza', 'pudim')
# print(lanche[2]) # mostra o item 2
# print(lanche[0:2]) # mostra do item 0 ao item 1 (o item 2 é ignorado)
# print(lanche[1:]) # mostra do primeiro elemento até o último
# print(lanche[-1]) # mostra o último elemento
#print(lanchje[-2:]) #começa no penultimo e vai até o final (começa na pizza e vai até o pudim)
# len(lanche) # mostra quantos elementos tem lanche (no caso 4)

# for c in lanche: # para cada elemento em lanche..
#     print(c) # mostra cada elemento de lanche
geral = tuple()
# As tuplas são IMUTáVEIS
# Não da para substituir itens de uma tupla por outros


# lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim') # não precisa de parênteses
# # imutáveis
# # lanche[1] = 'Refrigerante' # não pode substituir
# print(lanche[1])

lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita') # não precisa de parênteses


# for comida in lanche:
#     print(f'Eu vou comer {comida}') # mostra Eu vou comer Hambúrguer...etc

# for cont in range(0, len(lanche)):
#     print(cont) # mostra 0 1 2 3 4 já que ele ignora o ultimo numero, o len de lanche vai de 1 a 5 


for cont in range(0, len(lanche)):
    print(lanche[cont]) # mostra Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita'

# for cont in range(0, len(lanche)):
#     print(f'Eu vou comer {lanche[cont]}') # mostra Eu vou comer Hambúrguer...etc

# for cont in range(0, len(lanche)):
#     print(f'Eu vou comer {lanche[cont]} na posição {cont}') # mostra Eu vou comer Hambúrguer na posição 0...etc

# for pos, comida in enumerate(lanche):
#     print(f'Eu vou comer {comida} na posição {pos}') # mostra Eu vou comer Hambúrguer na posição 0...etc


# print(sorted(lanche)) # mostra a tupla em ordem (no caso ordem alfabética)
# print('Comi pra caramba!')

# a = (2, 5, 4)
# b = (5, 8, 1, 2)
# c = a + b
# print(c) # se cria uma tupla c, junta a tubla a e b e mostra (2, 5, 4, 5 ,8, 1, 2)

# print(len(c)) # Mostra quantos elementos tem c (no caso 7)

# print(c.count(5)) # mostra quantas vezes está aparecendo o número 5

# print(c.index(8)) # mostra em que posição está o 8 (posição 4 no caso)

# print(c.index(5)) # mostra e que posição está o primeiro 5 

# print(c.index(5, 3)) # mostra e que posição está o primeiro 5 a paritr da posição 3 (está na posição 3 no caso)

# pessoa = ('Gustavo', 39, 'M', 99.88) # se pode guardar valores diferentes em uma mesma dupla
# del(pessoa) # apaga a variavel tupla
# del(pessoa[0]) # não se pode apagar um único elemento da tupla
# print(pessoa) # não mostra porque foi apagado