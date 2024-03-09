# LISTAS 2
# Listas dentro das listas

# dados = []
# dados.append('Pedro') # adiciona elementos na lista
# dados.append(25)
# # print(dados[0])
# # print(dados[1])

# dados2 = []
# dados2.append('Maria') # adiciona elementos na lista
# dados2.append(19)

# dados3 = []
# dados3.append('João') # adiciona elementos na lista
# dados3.append(32)

# pessoas = []
# pessoas.append(dados[:]) # copia os dados da lista 'dados = []' e coloca dentro da lista 'pessoas = []' e dentro do elemento 0 vai ter os dados 'Pedro' e 25
# pessoas.append(dados2[:])
# pessoas.append(dados3[:])
# print(pessoas) # mostra: [['Pedro', 25], ['Maria', 19], ['João', 32]]
# print(pessoas[0]) # mostra: ['Pedro', 25]
# print(pessoas[0][0]) # mostra: Pedro # Pois esta na lista 0 e o nome Pedro esta dentro desssa lista 0 no índice 0
# print(pessoas[1][1]) # mostra: 19 # pois esta na lista 1 e no indice 1 dessa lista 1
# print(pessoas[2][0]) # mostra João pois esta na lista 2 e no indice 0 dessa lista 2

#=============================================================================================================================

#AULA PRATICA
# EX1

# teste = list()
# teste.append('Gustavo')
# teste.append(40)

# galera = list()
# galera.append(teste)
# teste[0] = 'Maria'
# teste[1] = 22
# galera.append(teste)
# print(galera) # Desse jeito mostra: [['Maria', 22], ['Maria', 22]]
# # ----------------------------------------------------------------
# teste = list()
# teste.append('Gustavo')
# teste.append(40)

# galera = list()
# galera.append(teste[:]) #cópia da lista
# teste[0] = 'Maria'
# teste[1] = 22
# galera.append(teste[:]) # cópia da lista
# print(galera) # Desse jeito mostra: [['Gustavo', 40], ['Maria', 22]]
#=====================================================================
# EX2
# galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]] # Declarando listas dentro de uma lista
# for p in galera:
#     print(p[0]) # mostra: os nomes João Ana Joaquim Maria

# for p in galera:
#     print(p[1]) # mostra: as idades 19 33 13 45

# for p in galera:
#     print(f'{p[0]} tem {p[1]} anos de idade.') # mostra nome e idade de todos: João tem 19 anos de idade. 
#=========================================================================================================
#EX3
# galera = list()
# dado = list()
# for c in range(0,3): # Preencer nome e idade de 3 pessoas
#     dado.append(str(input('Nome: ')))
#     dado.append(int(input('Idade: ')))
#     galera.append(dado[:])
#     dado.clear()

# print(galera) # mostra: [['Ana', 12], ['Joao', 22], ['Maria', 33]]

#EX 3.1

# galera = list()
# dado = list()
# for c in range(0,3): # Preencer nome e idade de 3 pessoas
#     dado.append(str(input('Nome: ')))
#     dado.append(int(input('Idade: ')))
#     galera.append(dado) # a lista galera e dados ficam ligados
#     dado.clear()

# print(galera) # mostra: [[], [], []] já que galera e dados estão ligados

# EX 3.2


galera = list()
dado = list()
totmai = totmen = 0 # só pode fazer com variaveis simples
for c in range(0,3): # Preencer nome e idade de 3 pessoas
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:]) 
    dado.clear()

for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior da idade.')
        totmai+=1
    else:
        print(f'{p[0]} é menor da idade.')
        totmen+=1

print(f'Temos {totmai} maiores e {totmen} menores de idade.')