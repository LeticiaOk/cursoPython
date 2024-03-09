# FUNÇÕES

# EX 1

# def mostralinha():
#     print('-' *  30)


# mostralinha() # mostra --------------------------
# print('SISTEMA DE ALUNOS')
# mostralinha()
# mostralinha()
# print('CADASTRO DE FUNCIONÁRIOS')
# mostralinha()
# mostralinha()
# print('ERRO DO SISTEMA')
# mostralinha()
# ====================================================

# FUNÇÕES COM PARÂMETRO

# EX 2

# def mensagem(msg): # Cria um parametro dentro dos parenteses (msg)
#     print('--------------------')
#     print(msg) # mostra a mensagem 'SISTEMA DE ALUNOS'
#     print('--------------------')
# 

# mensagem('SISTEMA DE ALUNOS') # Adiciona a mensagem 'SISTEMAS DE ALUNOS' ao parametro (msg)
# ===========================================================================================

# EX 3

# def titulo(txt):
#     print('-' * 30)
#     print(txt)
#     print('-' * 30)


# titulo('CURSO EM VÍDEO')
# titulo('PYTHON É MUITO BOM')

# Vai mostrar as duas mensagens: 
# ------------------------------
# CURSO EM VÍDEO
# ------------------------------
# ------------------------------
# PYTHON É MUITO BOM
# ------------------------------

# ==============================================================================================

# AULA PRÁTICA

# EX 1

# def soma(a,b):
#     s = a + b
#     print(s)


# Programa principal
# soma(4, 5)
# soma(8, 9)
# soma(2,1)
## soma(4) # Da erro já que soma recebe dois parametros a e b

# Mostra os resultados:
# 9
# 17
# 3
#===============================================================================================

# EX 2 

# def soma(a,b):
#     s = a + b
#     print(s)


# # Programa principal
# soma(a=4, b=5) # pode colocar os valores explicitamente

# # Mostra o resultado:
# # 9

#===================================================================================================

# EX 3

# def soma(a,b):
#     print(f'A = {a} e B = {b}')
#     s = a + b
#     print(f'A soma A + B = {s}')


# # Programa principal
# soma(b=4, a=5) # Pode trocar a ordem e precisa explicitar os dois
# soma(7, 2) # Se não explicitar ele vai na ordem (primeiro valor é a e segundo valor é b)
# Mostra:
# A = 4 e B = 5
# A soma A + B = 9
# A = 7 e B = 2
# A soma A + B = 9
#====================================================================================================

# EMPACOTAMENTO DE PARÂMETROS

# EX 1

# def contador(*num): # permite quantidades diferentes de valores para cada parametro
#     print(num)


# contador(2,1,7)
# contador(8,0)
# contador(4,4,7,6,2)

# # mostra as tuplas com os valores:

# # (2, 1, 7)
# # (8, 0)
# # (4, 4, 7, 6, 2)
#====================================================================================================

# EX 2

# def contador(*num): # permite quantidades diferentes de valores para cada parametro
#     for valor in num:
#         print(valor)


# contador(2,1,7)
# contador(8,0)
# contador(4,4,7,6,2)

# mostra:
# 2
# 1
# 7
# 8
# 0
# 4
# 4
# 7
# 6
# 2

#=========================================================================================================

# EX 2

# def contador(*num):
#    tam = len(num)
#    print(f'Recebi os valores {num} e são ao todo {tam} números')


# contador(2,1,7)
# contador(8,0)
# contador(4,4,7,6,2)

# mostra:
# Recebi os valores (2, 1, 7) e são ao todo 3 números
# Recebi os valores (8, 0) e são ao todo 2 números
# Recebi os valores (4, 4, 7, 6, 2) e são ao todo 5 números
#==========================================================================================================

# EX 3

# def dobra(lst):
#     pos = 0
#     while pos < len(lst):
#         lst[pos]*=2
#         pos+=1

# valores = [6,3,9,1,0,2]
# dobra(valores) # coloca a lista como parametro (lst)
# print(valores)

# mostra:
# [12, 6, 18, 2, 0, 4]
#==========================================================================

# EX 4

# def soma(* valores):
#     s = 0
#     for num in valores:
#         s += num
#     print(f'Somando os valores {valores} temos {s}')

# soma(5,2)
# soma(2.9,4)

# # mostra:

# Somando os valores (5, 2) temos 7
# Somando os valores (2.9, 4) temos 6.9
