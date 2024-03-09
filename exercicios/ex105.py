"""
Faça um programa que tenha uma função notas() que
pode receber várias notas de alunos e vai retornar
um dicionario com as seguintes informações:

- Quantidade de notas
- A maior nota
- A menor nota
- A média da turma
- A situação (opcional)

Mencione também docstrings na função
"""

# def notas(*n,sit=False):
#     """
#     -> Função para analisar notas e situações de vários alunos.
#     :param n: uma ou mais notas dos alunos (aceita várias)
#     :param sit: valor opcional, indicando se deve ou não adicionar a situação.
#     :return:  dicionário com várias informações sobre a situação da turma.

#     """
#     ficha = {}
#     total = len(n)
#     maior = max(n)
#     menor = min(n)
#     media = sum(n) / total

#     if media < 6:
#         situacao = 'RUIM'
#     elif media >= 6 and media < 7:
#         situacao = 'RAZOAVEL'
#     else:
#         situacao = 'BOA'
    
#     ficha['total'] = total
#     ficha['maior'] = maior
#     ficha['menor'] = menor
#     ficha['média'] = media
#     ficha['situação'] = situacao

#     if sit == False:
#         del ficha['situação']
    
#     return ficha
    
# # Programa principal
# resp = notas(5.5,9.5,10,6.5, sit=True)
# print(resp)

# RESULUÇÃO
def notas(*n, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma.
    """
    r =  dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n)/len(n)
    if sit:
        if r['média'] >= 7:
            r['situação'] = 'BOA'
        elif r['média'] >= 5:
            r['situação'] = 'RAZOÁVEL'
        else:
            r['situação'] = 'RUIM'

    return r


# Programa principal
resp = notas(5.5, 2.5, 1.5, sit=True)
print(resp)
help(notas)