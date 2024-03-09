def aumentar(preco=0, taxa=0, formato=False):
    """
    -> Calcula o aumento de um determinado preço,
    retornando o resultado com ou sem formatação.
    :param preco: o preço que se quer reajustar.
    :param taxa: qual é a porcentagem do aumento.
    :param formato: quer a saída formatada ou não?
    :return: o valor rajustado, com ou sem formato.
    """
    res = preco + (preco * taxa / 100)
    return res if formato is False else moeda(res)


def diminuir(preco=0, taxa=0, formato=False):
    res =  preco - (preco * taxa / 100)
    return res if formato is False else moeda(res)


def dobro(preco=0, formato=False):
    res = preco  * 2
    return res if not formato else moeda(res)


def metade(preco=0, formato=False):
    res =  preco / 2
    return res if not formato else moeda(res)


def moeda(preco = 0, moeda = 'R$'):
    return f'{moeda}{preco:>.2f}'.replace('.', ',')

def resumo(preco=0, taxaa=10, taxar=5):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço a ser analisado: \t{moeda(preco)}')
    print(f'Dobro do preço: \t{dobro(preco, True)}')
    print(f'Metado do preço: \t{metade(preco, True)}')
    print(f'{taxaa}% de aumento: \t{aumentar(preco, taxaa, True)}')
    print(f'{taxar}% de redução: \t{diminuir(preco, taxar, True)}')
    print('-' * 30)
   