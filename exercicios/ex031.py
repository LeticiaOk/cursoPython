# distancia = float(input('Digite a distância da viagen em Km: '))
# curta = 0.50 * distancia
# longa = 0.45 * distancia

# if distancia <= 200:
#     print('Sua viagem é curta.')
#     print('Preço da viagem: R${}'.format(curta))
# else:
#     print('Sua viagem é longa.')
#     print('Preço da viagem: {}'.format(longa))

# distancia =  float(input('Qual a distância da sua viagem? '))
# print('Você está prestes a começar uma viagem de {}Km.'.format(distancia))
# if distancia <= 200:
#     preco = distancia * 0.50 
# else:
#     preco =  distancia * 0.45
# print('E o preco da sua passagem será de R${:.2f}'.format(preco))

distancia =  float(input('Qual a distância da sua viagem? '))
print('Você está prestes a começar uma viagem de {}Km.'.format(distancia))
preco = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print('E o preco da sua passagem será de R${:.2f}'.format(preco))
