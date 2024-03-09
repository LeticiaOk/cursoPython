# from datetime import date
# ano = date.today().year
# maior = 0
# menor = 0
# for c in range(1,8):
#     nascimento = int(input('Em que a no a {}° pessoa nasceu? '.format(c)))
#     if ano - nascimento < 21:
#         menor += 1
#     else:
#         maior += 1
# print('Ao todo tivemos {} pessoas maiores de idade'.format(maior))
# print('E também tivemos {} pessoas menores de idade'.format(menor))

from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pess in range (1,8):
    nasc = int(input('Em que ano a {}° pessoa nasceu? '.format(pess)))
    idade = atual - nasc

    if idade >= 21:
        print('Essa pessoa é maior')
        totmaior += 1
    else:
        print('Essa pessoa é menor')
        totmenor += 1
        
print('Ao todo tivemos {} pessoas maiores de idade'.format(totmaior))
print('E tambpem ao todo tvemos {} pessoas menores de idade'.format(totmenor))