# import random
# aluno1 = input('Aluno 1: ')
# aluno2 = input('Aluno 2: ')
# aluno3 = input('Aluno 3: ')
# aluno4 = input('Aluno 4: ')

# print('Primero {}'.format(random.randint(1,4)))
# print('Segundo {}'.format(random.randint(1,4)))
# print('Terceiro {}'.format(random.randint(1,4)))
# print('Quarto {}'.format(random.randint(1,4)))

from random import shuffle
n1 = str(input('Primeiro nome: '))
n2 = str(input('Segundo nome: '))
n3 = str(input('Terceiro nome: '))
n4 = str(input('Quarto nome: '))

lista = [n1,n2,n3,n4]
shuffle(lista)
print('A ordem de apresentção será:')
print(lista)