# casa = float(input('Digite o valor da casa: '))
# salario = float(input('Digite seu salário: '))
# anos = int(input('Digite em quantos anos pagará o empréstimo: '))

# calculo1 = (salario*30)/100
# calculo2 = anos*12
# calculo3 = casa/calculo2


# if calculo3 > calculo1:
#     print('\033[33mEmpréstimo negado.\033[m')
# elif calculo3 <= calculo1:
#     print('\033[33mEmpréstimo aprovado.\033[m')


casa = float(input('Valor da casa: R$'))
salario = float(input('Salário do comprador: '))
anos = int(input('Quantos anos de financiameno? '))

prestacao = casa / (anos * 12)
minimo = salario * 30 / 100
print('Para pagar uma casa de R${:.2f} em {} anos'.format(casa, anos), end='')
print (' a prestação será de R${:.2f}'.format(prestacao))

if prestacao <= minimo:
    print('Emespréstimo pode ser CONCEDIDO!')
else:
    print('Empréstimo negado!')