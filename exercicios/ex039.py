# from datetime import date
# nascimento = int(input('Digite o ano de seu nascimento: '))
# ano = date.today().year
# idade = ano - nascimento

# if idade < 18:
#     print('Você ainda vai se alistar ao serviço militar.')
#     print('Faltam {} ano(s) para você se alistar.'.format(18-idade))
# elif idade == 18:
#     print('É hora de se alistar ao serviço militar.')
# elif idade > 18:
#     print('O tem de alistamento já passou')
#     print('Se passaram {} ano(s) do prazo.'.format(idade-18))

from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, atual))
if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo = 18 - idade 
    print('Ainda faltam {} anos para o alistamento'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento será em {}.'.format(ano))
else:
    saldo = idade - 18
    print('Você já deveria ter se alistado há {} anos '.format(saldo))
    ano = atual - saldo
    print('Seu alistameto foi em {}.'.format(ano))