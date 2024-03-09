# print(pow(4,3)) #potência
# print(81**(1/2)) #raiz quadrada
# print(127**(1/3)) #raiz cúbica

# print('Oi'+'Olá')
# print('Oi'*5)
# print('='*28)

# nome = str(input('Qual é o seu nome? '))
# print('Prazer em te conhecer {:=^20}!'.format(nome))

n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1//n2
e = n1 **n2
print('A soma é {}, \n o produto é {} e a \n divisão é {:.3f}'.format(s, m, d), end='>>>')
print('Divisão inteira {} e potência {}'.format(di, e))