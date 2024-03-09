# MÓDULOS E PACOTES

# MÓDULOS

# Criar uma pasta 'modulos'
# criar um arquivo para o programa principal 'numeros' 
# Criar um arquivo para as funções 'uteis'

# def fatorial(n):
#     f = 1
#     for c in range(1,n+1):
#         f *= c
#     return f


# def dobro(n):
#     return n * 2


# def triplo(n):
#     return n * 3


# Importar o arquivo das funções no arquivo do programa principal

# import uteis

# num = int(input('Digite um valor: '))
# fat = uteis.fatorial(num)
# print(f'O fatorial de {num} é {fat}.')
# print(f'O dobro de {num} é {uteis.dobro(num)}')

# ou

# from uteis import fatorial, dobro # pode dar conflito se tiver ou biblioteca com as mesmas funções

# num = int(input('Digite um valor: '))
# fat = fatorial(num)
# print(f'O fatorial de {num} é {fat}.')
# print(f'O dobro de {num} é {dobro(num)}')


# PACOTES
# É uma pasta que contém modulos

# Criar pasta chamada 'modulos'
# Criar arquivo chamado numeros.py (programa principal)
# Criar pasta chamada 'uteis'
# Criar aquirvo __init__.py dentro da pasta 'uteis'

# Criar mais pacotes

# Criar pasta com o nome do pacote 'numeros'
# Criar aquirvo __init__.py dentro da pasta 'numeros'
# Colocar a função dos npumeros dentro do arquivo  __init__.py  da pasta 'numeros'

def metade(num, form = False):
    result = num / 2
    if form == True:
        return moeda(result)
    else:
        return result


def dobro(num, form = False):
    result = num * 2
    if form ==  True:
        return moeda(result)
    else:
        return result
    

def aumentar(num, percent, form = False):
    percent = (num * percent) / 100
    result = percent + num
    if form == True:
        return moeda(result)
    else:
        return result


def diminuir(num, percent, form = False):
    percent = (num * percent) / 100
    result = num - percent
    if form ==  True:
        return moeda(result)
    else:
        return result


def moeda(num):
    return f'R${int(num)},00'


def resumo(num, incr, redu):
    print('-' * 30)
    print(f'{"RESUMO DO VALOR":^30}')
    print('-' * 30)

    print(f'{"Preço analisado:":20} {moeda(num):<10}')
    print(f'{"Dobro do preço":20} {moeda(dobro(num)):<10}')
    print(f'{"Metade do preço:":20} {moeda(metade(num)):<10}')
    print(f'{"80% de aumento:":20} {moeda(aumentar(num,incr)):<10}')
    print(f'{"35% de redução:":20} {moeda(diminuir(num,redu)):<10}') 
    print('-' * 30)
