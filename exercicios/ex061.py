"""

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = primeiro + (10 - 1) * razao
for c in range(primeiro, decimo + razao, razao):
    print('{}'.format(c), end=' → ')
print('ACABOU')

"""
# primeiro = int(input('Primeiro termo: '))
# razao = int(input('Razão: '))
# pa = primeiro
# cont = 0
# while cont <= 9:  
#     print(pa, end=' - ')
#     pa = pa + razao
#     cont += 1
# print('Fim')

print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
cont = 1
while cont <= 10:
    print('{} - '.format(termo),end='')
    termo += razao
    cont += 1
print('FIM')