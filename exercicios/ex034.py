# salario = float(input('Digite seu salário: '))
# dez = (salario*10)/100
# quinze = (salario*15)/100

# if salario > 1250.00:
#     print('Seu aumento será de 10%.')
#     print('Valor do aumento: R${:.2f}'.format(dez))
#     print('Valor total: R${:.2f}'.format(dez + salario))
# else:
#     print('Seu aumento será de 15%.')
#     print('Valor do aumento: R${:.2f}'.format(quinze))
#     print('Valor total: R${:.2f}'.format(quinze + salario))

salario = float(input('Qual o salário do funcionário? R$'))
if salario <= 1250:
    novo = salario + (salario * 15/100)
else:
    novo = salario + (salario * 10/100)
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(salario, novo))