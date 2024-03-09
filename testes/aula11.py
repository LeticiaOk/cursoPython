# \033[0;33;44m

# style
# 0 None
# 1 Bold
# 4 Underline
# 7 Negative o que colocou pra letra vai pra fundo e o que colocou no fundo vai pra letra.

# Text
# 30 Cinza
# 31 Vermelho
# 32 verde
# 33 Amarelo
# 34 Azul escuro
# 35 roxo(magenta)
# 36 ciano
# 37 Branco (cor padrão)

# Back
# 40 Branco
# 41 Vermelho
# 42 Verde
# 43 Amarelo
# 44 Azul escuro
# 45 roxo(magenta)
# 46 ciano
# 47 cinza

#\033[m (padrão)
#\033[7:30m letra preta fundo branco

# a = 3
# b = 5

# print('Os valores são: \033[32m{}\033[m e \033[31m{}\033[m!!!'.format(a, b))

# nome = 'Guanabara'
# print('Olá! uito prazer em te conhecer, {}{}{}!!!'.format('\033[4;34m',nome,'\033[m'))

nome = 'Guanabara'
cores = {'limpa':'\033[m',
        'azul': '\033[34m',
        'amarelo': '\033[33m',
        'pretoebranco': '\033[7;37m' }
print('Olá! uito prazer em te conhecer, {}{}{}!!!'.format(cores['pretoebranco'],nome,cores['limpa']))

#Desafio colocar cores nos exercicios 