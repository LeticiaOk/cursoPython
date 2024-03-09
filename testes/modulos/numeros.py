from uteis import numeros

num = int(input('Digite um valor: '))
fat = numeros.fatorial(num)
print(f'O fatorial de {num} é {fat}.')
print(f'O dobro de {num} é {numeros.dobro(num)}')

# ou

# from uteis import fatorial, dobro # pode dar conflito se tiver ou biblioteca com as mesmas funções

# num = int(input('Digite um valor: '))
# fat = fatorial(num)
# print(f'O fatorial de {num} é {fat}.')
# print(f'O dobro de {num} é {dobro(num)}')

