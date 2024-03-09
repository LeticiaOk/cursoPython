# from datetime import date
# nascimento = int(input('Digite sua data de nascimento: '))
# ano = date.today().year
# idade = (ano - nascimento)

# print('Idade: {}'.format(idade))
# if idade <= 9:
#     print('Categoria: \033[34mMirim\033[m')
# elif idade > 9 and idade <= 14:
#     print('Categoria : \033[34mInfantil\033[m')
# elif idade > 15 and idade <= 19:
#     print('Categoria: \033[34mJunior\033[m')
# elif idade > 19 and idade <= 20:
#     print('Categoria: \033[34mSênior\033[m' )
# elif idade > 20:
#     print('Categora: \033[34mMaster\033[m')

from datetime import date
atual = date.today().year
nascimento = int(input('Ano de nascimento: '))
idade =  atual - nascimento
print('O atleta tem {} anos.'.format(idade))

if idade <= 9:
    print('Classificação: MIRIM')
elif idade <= 14:
    print('Classificação: INFANTIL')
elif idade <= 19:
    print('Classificação: JUNIOR')
elif idade <= 25:
    print('Classificação: SÊNIOR')
else:
    print('Classificação: MASTER')