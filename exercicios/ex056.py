# soma = 0
# cont = 0
# idadevelho = 0
# nomevelho = ''
# for c in range(1,5):

#     nome = str(input('Nome da {}° pessoa: '.format(c)))
#     idade = int(input('Idade: '))
#     soma +=idade
#     sexo = str(input('Sexo: ([M] para "Masculino" | [F] para "Feminino") ')).upper()
    
#     if idade < 20 and sexo == 'F':
#         cont = cont + 1
#     if idade > idadevelho and sexo == 'M':
#         idadevelho = idade
#         nomevelho = nome
        

# print('A média de idade do grupo é: {:.0f} anos'.format(soma/4))
# print('Total de mulheres com menos de 20 anos: {}'.format(cont))
# print('Nome do homem mais velho: {}'.format(nomevelho))
# print('Idade do homem mais velho: {}'.format(idadevelho))

somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
for p in range (1, 5):

    print('---- {}ª PESSOA ----'.format(p))

    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F]: ')).strip()
    somaidade += idade
   
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade > 20:
        totmulher20 += 1

mediaidade = somaidade /4

print('A média de idade do grupomé de {} anos'.format(mediaidade))
print('O homem mais velho tem {} anos e se chama {}'.format(maioridadehomem, nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(totmulher20))