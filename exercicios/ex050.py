# s = 0
# for c in range(1,7):
#    n = int(input('Digite o {}° número: '.format(c)))
#    if n % 2 == 0:
#         s += n
# print('A soma dos números pares é de: {}'.format(s))

soma = 0
cont = 0
for c in range(1, 7):   
        num = int(input('Digite o {}° valor: '.format(c)))
        if num % 2 == 0:
                soma += num
                cont += 1
print('Você informou {} números PARES e a soma doi {}'.format(cont, soma))