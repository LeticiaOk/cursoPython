# nome = input('Digite seu nome inteiro: ')
# maiusculo = nome.upper()
# print('Tem "SILVA" no nome? {}'.format('SILVA' in maiusculo))

nome = str(input('Qual seu nome completo: ')).strip()
print('Seu nome tem Silva? {}'.format('silva' in nome.lower()))