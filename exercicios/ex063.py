
# primeiro = int(input('Primeiro termo: '))
# razao = int(input('Razão: '))
# pa = primeiro
# cont = 0
# while cont <= 9:  
#     print(pa, end=' - ')
#     pa = pa + razao
#     cont += 1
# print('Fim')

# cont = 0
# calculo = 0

# termo = int(input('Quantos termos você quer mostrar? '))
# while cont <= termo - 1:
#     calculo = calculo + cont
#     cont += 1
#     print(calculo,' - ',cont, end=' - ')
# print('Fim')

print('Sequência de Fibonacci')
print('-' * 30)
n  = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
print('~' * 30)
print('{} -> {}'.format(t1,t2), end='')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(' -> {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    cont += 1
print(' -> FIM')
print('~' * 30)

