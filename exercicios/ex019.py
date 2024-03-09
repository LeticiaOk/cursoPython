# import random
# aluno1 = (input('Aluno 1: '))
# aluno2 = (input('Aluno 2: '))
# aluno3 = (input('Aluno 3: '))
# aluno4 = (input('Aluno 4: '))
# resultado = random.randint(1, 4)
# print('O sorteado foi o aluno: {}'.format(resultado))

from random import choice
n1 = str(input('Primeiro nome: '))
n2 = str(input('Segundo nome: '))
n3 = str(input('Terceiro nome: '))
n4 = str(input('Quarto nome: '))

lista = [n1,n2, n3,n4]
escolhido = choice(lista)
print('O aluno escolhido foi {}'.format(escolhido))