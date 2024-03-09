# valor = float(input('Digite o valor do produto: '))
# pagamento = input('Digite a forma de pagamento: ')
# desc10 = valor - ((valor*10)/100) 
# desc5 = valor - (valor*5)/100
# parc2 = valor/2


# if pagamento == 'dinheiro':
#     print('O valor com 10% de desconto será de: {}'.format(desc10))
# elif pagamento == 'cartão':
#     forma = input('Digite [a] para pagamento a vista ou [b] para pagamento parcelado: ')
#     if forma == 'a':
#         print('O valor a vista com 5% de desconto será de {}'.format(desc5))
#     elif forma == 'b':
#         parcela = int(input('Digite o número de parcelas :'))
#         if parcela == 2:
#             print('O valor dar parcelas serão de: {}'.format(parc2))
#         elif parcela > 2:
#             print('O valor será de {} mais os 20% de juros'.format(valor/parcela + (valor*0.20)))

print('{:=^40}'.format(' LOJAS GUANABARA '))
preco = float(input('Preço das compras: R$'))
print('''FORAS DE PAGAMENTO
[1] à vsta dinheiro/cheque
[2] à vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão''')
opcao = int(input('Qual é a opção? '))

if opcao == 1:
    total = preco - (preco * 10 / 100)
elif opcao  == 2:
    total = preco - (preco * 5 / 100)
elif opcao == 3:
    total = preco
    parcela = total/2
    print('Sua compra será parcelada em 2x de R${:.2f} SEM JUROS'.format(parcela))
elif opcao == 4:
    total = preco + (preco * 20/100)
    totparc = int(input('Quantas parcelas? '))
    parcela = total/totparc
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(totparc,parcela))
else:
    total = preco
    print('OPÇÃO INVÁLIDA de pagamento. Tente novamente')
print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preco, total))