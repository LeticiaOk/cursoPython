# num = 0
# while True:
#     num = int(input('Digite um número par ver sua tabuada (negativo encerra o programa): '))
#     if num < 0:
#         break
#     for i in range (1,11):
#         print(f'{num} x {i} = {num*i}')
# print('\033[31mPrograma encerrado!\033[m')

while True:
    n = int(input('Quer ver a tabuada de qula valor? '))
    print('-' * 30)
    if n < 0:
        break
    for c in range(1,11):
        print(f'{n} x {c} = {n*c}')
    print('-' * 30)
print('PROGRAMA TABUADA ENCERRAODO. Volte sempre!')