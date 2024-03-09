# valores = []
# while True:
#     num = int(input('Digite um valor: '))
#     if num not in valores:
#           valores.append(num)
#           print('\033[32mValor adicionado com sucesso!\033[m')
#     else:
#          print('\033[31mOps..valores duplicados não serão adiconados a lista\033[m')

#     resp = input('Deseja continuar? [S/N]: ').upper()

#     while resp != 'S' and resp != 'N':
#          resp = input('Opção inválida. Ultilize \033[32m[S]\033[m para \033[32mSIM\033[m ou \033[31m[N]\033[m para \033[31mNÃO\033[m: ').upper()
    
#     if resp == 'N':
#          break

# valores.sort()
# print(f'Você digitou os valores: {valores}')

#RESOLUÇÃO
numeros = list()
while True:
     n = int(input('Digite um valor: '))
     if n not in numeros:
        numeros.append(n)
        print('Valor adicionado com sucesso...')
     else:
        print('Valor duplicado! Não vou adicionar...')
    
     r = str(input('Quer continuar: [S/N] '))
     if r in 'Nn':
        break
print('-=' * 30)
numeros.sort()
print(f'Você digitou os valores {numeros}')

