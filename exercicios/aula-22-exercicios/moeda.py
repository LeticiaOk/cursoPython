def metade(num, form = False):
    result = num / 2
    if form == True:
        return moeda(result)
    else:
        return f'{result:.2f}'


def dobro(num, form = False):
    result = num * 2
    if form ==  True:
        return moeda(result)
    else:
        return f'{result:.2f}'
    

def aumentar(num, percent, form = False):
    percent = (num * percent) / 100
    result = percent + num
    if form == True:
        return moeda(result)
    else:
        return f'{result:.2f}'


def diminuir(num, percent, form = False):
    percent = (num * percent) / 100
    result = num - percent
    if form ==  True:
        return moeda(result)
    else:
        return f'{result:.2f}'


def moeda(num):
    novo = ''
    num = str(num)
    for i in num:
        if i != '.':
           novo+=i
        else:
           novo += ','
    if novo[-1] == '0' and novo[-2] == ',':
        novo+= '0'
    return f'R${novo}'
   


def resumo(num, incr, redu):
    print('-' * 30)
    print(f'{"RESUMO DO VALOR":^30}')
    print('-' * 30)

    print(f'{"Preço analisado:":20} {moeda(num):<10}')
    print(f'{"Dobro do preço":20} {moeda(dobro(num)):<10}')
    print(f'{"Metade do preço:":20} {moeda(metade(num)):<10}')
    print(f'{incr:2}{"% de aumento:":18} {moeda(aumentar(num,incr)):<10}')
    print(f'{redu:2}{"% de redução:":18} {moeda(diminuir(num,redu)):<10}') 
    print('-' * 30)
