# frase = str(''.join(input('Digite uma frase: ').split())).strip().upper()
# fraseInvertida = ''.join(frase[::-1].split())
# print(frase)
# print(fraseInvertida)


# FOR
# if frase == fraseInvertida:
#     print('Essa frase é um palíndromo')
# else:
#     print('Essa frase não é um palíndromo')

# frase = str(input('Digite uma frase: ')).strip().upper()
# palavras = frase.split()
# junto = ''.join(palavras)
# inverso = ''

# for letra in range(len(junto) - 1, -1, -1):
#     inverso += junto[letra]
# print('O inverso de {} é {}'.format(junto, inverso))
# if inverso == junto:
#         print('Temos um palíndromo!')
# else:
#         print('A frase digitada não é um palíndromo')


#FATIAMENTO
frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]

print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
        print('Temos um palíndromo!')
else:
        print('A frase digitada não é um palíndromo')
