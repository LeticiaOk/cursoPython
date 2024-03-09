# resposta = ''
# maior = 0
# menor = 0
# soma = 0
# cont = 0
# while resposta != 'não':
#     num = int(input('Digite um valor: '))
#     soma += num
#     cont+=1

#     if cont == 1:
#         maior = num
#         menor = num

#     else:
#         if num > maior:
#             maior = num
#         if num < menor:
#             menor = num

#     resposta = str(input('Deseja digitar mais um valor? '))
# print('Média dos valores: {:.2f}'.format(soma/cont))
# print('Maior valor: {}'.format(maior))
# print('Menor valor: {}'.format(menor))

resp = 'S'
soma = media = quant = maior = menor =0
while resp in 'Ss':
    num = int(input('Digite um número: '))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
media = soma / quant
print('Você digitou {} números e a média foi {}'.format(quant, media))
print('O maior valor foi {} e o manor foi {}'.format(maior, menor))
