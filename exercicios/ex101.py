"""
Cria um programa que tennha um função chamada voto()
que vai receber como parâmetro o ano de nascimento de
uma pessoa. retornando um valor literal indicando se
uma pessoa tem voto negado, opcional ou obrigatório
nas eleições.
"""


# def voto(nasc):
#     from datetime import date
#     global idade
#     ano = date.today().year
#     idade = ano - nasc
#     if idade >= 18 and idade < 65:
#         return 'VOTO OBRIGATÓRIO'
#     elif (idade >= 16 and idade < 18) or idade >= 65:
#         return 'VOTO OPCIONAL'
#     else:
#         return 'NÃO VOTA'
        
    

# put_nasc = int(input('Em que ano você nasceu? '))
# voto(put_nasc)
# print(f'Com {idade} anos: {voto(put_nasc)}.')

# RESOLUÇÃO

def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO'


# Programa Principal
nasc = int(input('Em que ano você nasceu? '))
print(voto(nasc))
