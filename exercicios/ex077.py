# palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 'estudar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')

# print(len(palavras))
# for c in range(0,len(palavras)):
#     print(f'\nNa palavra {palavras[c].upper()} temos:',end=' ')
    
    
#     contA = palavras[c].count('a')
#     print('A' * contA, end='')

#     contE = palavras[c].count('e')
#     print('E' * contE, end='')

#     contI = palavras[c].count('i')
#     print('I' * contI, end='')

#     contO = palavras[c].count('o')
#     print('O'* contO, end='')

#     contU = palavras[c].count('u')
#     print('U' * contU, end='')



palavras = ('aprender', 'programar', 'linguagem','python',
            'curso', 'gratis', 'estudar', 'praticar',
            'trabalhar', 'mercado', 'programador', 'futuro')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos ', end=' ')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')