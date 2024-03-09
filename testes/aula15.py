# cont  = 1
# while True: # Executa o código para sempre
#     print(cont, ' -> ',end='')
#     cont += 1
# print('Acabou') # Não aparece 

# COM GAMBIARRA
# n = s = 0
# cont = 0
# while n != 999:
#     n  = int(input('Digite um número: '))
#     s += n
# s -= 999 # gambiarra
# print('A soma vale {}'.format(s))

#SEM GAMBIARRA
# n = s = 0
# cont = 0
# while True:
#     n  = int(input('Digite um número: '))
#     if n == 999:
#         break # quebra o laço while e pula para o fim do programa 
#     s += n

# print('A soma vale {}'.format(s))

# F STRING
# n = s = 0
# cont = 0
# while True:
#     n  = int(input('Digite um número: '))
#     if n == 999:
#         break # quebra o laço while e pula para o fim do programa 
#     s += n

# print('A soma vale {}'.format(s))
# print(f'A soma vale {s}') # f string

# nome = 'José'
# idade = 33
# print(f'O {nome} tem {idade} anos') # python 3.6+
# print('O {} tem {} anos'.format(nome, idade)) # python 3
# print('O %s tem %d anos' %(nome, idade)) # python 2

# nome = 'José'
# idade = 33
# salario = 987.3
# print(f'O {nome:-<20} tem {idade} anos e ganha {salario} R${salario:.2f}')

