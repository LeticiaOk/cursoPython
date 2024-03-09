# maiorPeso = 0
# menorPeso = 1000
# for c in range (1,6):       
#     peso = float(input('Digite o peso da {}° pessoa: '.format(c)))
#     if peso > maiorPeso:
#         maiorPeso = peso
#     if peso < menorPeso:
#         menorPeso = peso
# print('O maior peso foi de {}Kg'.format(maiorPeso))
# print('O menor peso foi de: {}Kg'.format(menorPeso))


maior = 0
menor = 0

for p in range(1,6):
    peso = float(input('Peso da {}° pessoa: '.format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso lido foi de {}Kg'.format(maior))
print('O menor peso lido foi de {}Kg'.format(menor))
        