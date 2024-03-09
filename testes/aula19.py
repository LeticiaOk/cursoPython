# DICIONÁRIOS

#-------------------------------------------------------------------
# EXEMPLO 1

# dados = dict() # outra forma de declarar diconários
# dados = {'nome': 'Pedro', 'idade': 25}
# print(dados['nome']) # Pedro
# print(dados['idade']) # 15
# dados['sexo'] = 'M' # {'nome': 'Pedro', 'idade': 25, 'sexo': 'M'}
# # print(dados) 
# del dados['idade'] # apaga o elemento 'idade' e o seu valor 25
# -------------------------------------------------------------------

#-------------------------------------------------------------------
# EXEMPLOS 2

# filme = {'titulo': 'Star Wars',
#          'ano': 1977,
#          'diretor': 'George Lucas'} # Pode fechar chaves na outra linha
# print(filme.values()) # Mostra os valores:  dict_values(['Star Wars', 1977, 'George Lucas']) 
# print(filme.keys()) # Mostra as chaves: dict_keys(['titulo', 'ano', 'diretor'])
# print(filme.items()) # Mostra os itens: dict_items([('titulo', 'Star Wars'), ('ano', 1977), ('diretor', 'George Lucas')])

# for k, v in filme.items():
#     print(f'O {k} é {v}')   # Otitulo é Star Wars (1º laço)
#                             # O ano é 1977 2º laço)
#                             # O diretor é George Lucas 3º laço)
    
# locadora = []
# locadora.append(filme) # Pode-se ter um dicionário dentro de uma lista
# print(locadora) # [{'titulo': 'Star Wars', 'ano': 1977, 'diretor': 'George Lucas'}]
# print(locadora[0]) #{'titulo': 'Star Wars', 'ano': 1977, 'diretor': 'George Lucas'}
# print(locadora[0]['ano']) # 1977
#----------------------------------------------------------------------------------------------------------------------------

# AULA PRÁTICA

#-----------------------------------------------------------------------------------------------------
# EXEMPLO 1

# pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
# print(pessoas[0]) # da erro porque o elemento 0 é 'nome'
# print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos') # usar aspas duplas # O Gustavo tem 22 anos

#------------------------------------------------------------------------------------------------------
# EXEMPLO 1.1 MOSTRANDO VALORES

# for k in pessoas.keys():
#     print(k)    # nome
#                 # sexo
#                 # idade

# for k in pessoas.values():
#     print(k)    # Gustavo
#                 # M
#                 # 22

# for k, v in pessoas.items():
#     print(f'{k} = {v}')   # nome = Gustavo
                            # sexo = M
                            # idade = 22
# -------------------------------------------------------------------------------------------------------

# EXEMPLO 1.2 TRABALHANDO COM DICIONARIOS


# del pessoas['sexo'] # APAGOU
# for k, v in pessoas.items():
#     print(f'{k} = {v}')   # nome = Gustavo
                            # idade = 22

# pessoas['nome'] = 'Leandro' # SUBSTITUIU
# for k, v in pessoas.items():
#     print(f'{k} = {v}') # nome = Leandro
                        # sexo = M
                        # idade = 22

# pessoas['peso'] = '98.5' # ADICIONOU
# for k, v in pessoas.items():
#     print(f'{k} = {v}') # nome = Gustavo
                        # sexo = M
                        # idade = 22
                        # peso = 98.5

# -----------------------------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------------------------
# EXEMPLO 2

# ADICIONANDO DICIONÁRIOS DENTRO DE LISTAS

# brasil = []
# estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
# estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
# brasil.append(estado1)
# brasil.append(estado2)

# print(estado1) # {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
# print(estado2) # {'uf': 'São Paulo', 'sigla': 'SP'}

# print(brasil) # [{'uf': 'Rio de Janeiro', 'sigla': 'RJ'}, {'uf': 'São Paulo', 'sigla': 'SP'}]
# print(brasil[0]) # {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
# print(brasil[0]['uf']) # Rio de Janeiro
# print(brasil[1]['uf']) # São Paulo
#------------------------------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------------------------
# EXEMPLO 3

# MANEIRA CERTA E ERRADA DE MOSTRAR DICIONARIOS DENTRO DE LISTAS

# estado = dict()
# brasil = list()

# for c in range (0, 3):
#     estado['uf'] = str(input('Unidade Federativa: '))
#     estado['sigla'] = str(input('Siglado do Estado: '))
#     brasil.append(estado) # ERRADO

# print(brasil) # ERRADO: [{'uf': 'Acre', 'sigla': 'AC'}, {'uf': 'Acre', 'sigla': 'AC'}, {'uf': 'Acre', 'sigla': 'AC'}]



# estado = dict()
# brasil = list()

# for c in range (0, 3):
#     estado['uf'] = str(input('Unidade Federativa: '))
#     estado['sigla'] = str(input('Siglado do Estado: '))
#     brasil.append(estado.copy()) # CERTO

# print(brasil) # CERTO: [{'uf': 'MINAS GERAIS', 'sigla': 'MG'}, {'uf': 'ACRE', 'sigla': 'AC'}, {'uf': 'GOIAS', 'sigla': 'GO'}]


# -----------------------------------------------------------------------------------------------------------------------
# EX 3.1

# estado = dict()
# brasil = list()

# for c in range (0, 3):
#     estado['uf'] = str(input('Unidade Federativa: '))
#     estado['sigla'] = str(input('Siglado do Estado: '))
#     brasil.append(estado.copy()) 

# for e in brasil:
#     for k, v in e.items():
#         print(f'O campo {k} tem valor {v}') # O campo uf tem valor rio de janeiro
                                              # O campo sigla tem valor rj
                                              # O campo uf tem valor goias
                                              # O campo sigla tem valor go
                                              # O campo uf tem valor sao paulo
                                              # O campo sigla tem valor sp

# -----------------------------------------------------------------------------------------------------------------------
# EXEMPLO 3.2

# estado = dict()
# brasil = list()

# for c in range (0, 3):
#     estado['uf'] = str(input('Unidade Federativa: '))
#     estado['sigla'] = str(input('Siglado do Estado: '))
#     brasil.append(estado.copy()) # CERTO

# for e in brasil:
#     for v in e.values():
#         print(v, end=' ')
#     print()     # Acre AC
#                 # Amazonas AM
                  # Pará PA

n = ' '
print(n.isspace())