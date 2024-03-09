# FUNÇÕES PARTE 2

# AJUDA ITERATIVA

# Maneira 1.
# Digitar python no terminal para abrir o console
# Digitar help()
# Escrever o comando que quer obter informações

# Maneira 2.
# help(print) # Mostra informações sobre o print

# Maneira 3.
# print(input.__doc__) # Mostra informações sobre input

#-----------------------------------------------------

# DOCSTRINGS

# def contador(i,f,p):
#     """
#     -> Faz uma contagem e mostra na tela.
#     :param i: início da contagem
#     :param f: fim da contagem
#     :param p: passo da contagem
#     :return: sem retorno
#     """
#     c = i
#     while c <= f:
#         print(f'{c}', end=' ')
#         c+=p
#     print('FIM!')


# help(contador)

# -------------------------------------------------------------------

# PARÂMETROS OPCIONAIS

# def somar(a=0,b=0,c=0): # Faz com que os parâmetros recebam valor 0
#     s = a + b + c
#     print(f'A soma vale {s}')

# somar(3,2,5)
# somar(8,4) # adicionado nenhum valor ao parâmetro c ele vai continuar a valer 0
# somar() # a,b,c valem 0
# somar(b=4,c=2) # a vale 0
# somar(c=3, a=2) # b vale 0

# -------------------------------------------------------------------------------

# ESCOPO DE VARIÁVEIS

#EX 1

# def teste():
#     x = 8 # Variavel local (só funciona dentro do ESCOPO LOCAL no caso a área da função)
#     print(f'Na função teste n vale {n}')
#     print(f'Na função teste, x vale {x}')
# # Programa principal
# n = 2 # Varialvel global (funciona no ESCOPO GLOBAL no caso em toda a área do programa)
# print(f'No programa principal, n vale {n}')
# teste()
# print(f'No programa principal, x vale {x}') # Erro já que x é uma varial local da função

# EX 2

# def teste(b):
#     a = 8 # varivel local a (o programa agora tem duas variaveis a uma local valendo 8 e outra global valendo 5) 
#     b += 4 # soma com a global
#     c = 2
#     print(f'A dentro vale {a}') # mostra 8
#     print(f'B dentro vale {b}') # mostra 9
#     print(f'C dentro vale {c}') # mostra 2

# a = 5
# teste(a)
# print(f'A fora vale {a}') # mostra 5

# EX 3

# def teste(b):
#     global a # Não cria outra variavel local a e usa a variavel global a fazendo com que ela passe a valer 8
#     a = 8 
#     b += 4 # soma com a global (5)
#     c = 2
#     print(f'A dentro vale {a}') # mostra 8
#     print(f'B dentro vale {b}') # mostra 9
#     print(f'C dentro vale {c}') # mostra 2

# a = 5 # vai passar a valer 8
# teste(a)
# print(f'A fora vale {a}') # mostra 8

# ---------------------------------------------------------------------------------------------------------------------

# RETORNO DE VALORES

# def somar(a=0, b=0, c=0):
#     s = a + b + c
#     return s # a função def somar(a=0, b=0, c=0) retorna o resultado de s para r1 = somar(3,2,5), r2 = somar(2,2) e r3 = somar(6)

# r1 = somar(3,2,5) # print(somar(3,2,5)) faz aparecer na tela o return da função no caso 10
# r2 = somar(2,2)
# r3 = somar(6)
# print(f'Meus cálculos deram {r1}, {r2} e {r3}.') # Meus cálculos deram 10, 4 e 6.

# -----------------------------------------------------------------------------------------------------------------------

# AULA PRÁTICA

# EX 1

# def fatorial(num=1):
#     f = 1
#     for c in range(num, 0, -1):
#         f *= c
#     return f


# n = int(input('Digite um número: ')) # 5
# print(f'O fatorial de {n} é igual a {fatorial(n)}') # O fatorial de 5 é igual a 120

#----------------------------------------------------------------------------------------------

# EX 2

# def fatorial(num=1):
#     f = 1
#     for c in range(num, 0, -1):
#         f *= c
#     return f


# f1 = fatorial(5)
# f2 = fatorial(4)
# f3 = fatorial()
# print(f'Os valores são {f1}, {f2} e {f3}')

#-----------------------------------------------------------------------------------------------

# def par(n=0):
#     if n % 2 == 0:
#         return True
#     else:
#         return False
    

# num = int(input('Digite um número: '))
# if par(num): # se return for True 
#     print('É par')
# else: # se for False
#     print('Não é par')
help(len)