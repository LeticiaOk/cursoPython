# print('-=-'*20)
# print('Analisador de triângulos')
# print('-=-'*20)

# r1 = float(input('Primeiro segmento: '))
# r2 = float(input('Segundo segmento: '))
# r3 = float(input('Terceiro segmento: '))

# if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
#     print('Os segmentos acima PODEM FORMAR triângulo!')
#     if r1 == r2 and r1 == r3 and r2 == r3:
#         print('Equilátero: Todos os lados são iguais.')

#     elif r1 != r2 and r1 != r3 and r2 != r3:
#         print('Escaleno: Todos os lados diferentes.')

#     elif r1 == r2 and r1 != r3 and r2 != r3:
#         print('Isósceles: Dois lados iguais.')
#     elif r1 == r3 and r1 != r2 and r2 != r3:
#         print('Isósceles: Dois lados iguais')
#     elif r2 == r3 and r1 != r2 and r1 != r3:
#         print('Isósceles: Dois lados iguais')
# else:
#     print('Os segmentos acima NÃO PODEM FORMAR triângulo')


r1 =  float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR triângulo ', end='')
    # if r1 == r2 and r2 == r3 
    if r1 == r2 == r3:
        print('EQUILÁTERO ')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO')
    else:
        print('ISÓSCELES')
else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo')

