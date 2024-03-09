valores = []
cont = 0
while True:
    valores.append(int(input('Digite um valor: ')))
    cont+= 1

    resp = input('Deseja continuar? [S/N]: ').upper()

    while resp != 'N' and resp != 'S':
       resp = input('Opção inválida, apenas [S] para SIM ou [N] para NÃO: ').upper()
    
    if resp == 'N':
     break
print('-' * 40)
print(f'Total de valores digitados: {cont}')
valores.sort(reverse=True)
print(f'Valores em ordem decrescente: {valores}')
if 5 in valores:
   print('O valor 5 faz parte da lista')
else:
   print('O valor 5 não faz parte da lsita')