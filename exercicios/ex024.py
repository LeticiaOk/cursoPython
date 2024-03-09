# cidade = input('Digite o nome de uma cidade: ')
# conversao = cidade.upper()
# divisao = conversao.split()

# print('A cidade começa com SANTO? {}'.format('SANTO' in divisao[0]))

cid = str(input('Em que cidade você nasceu? ')).strip()
print(cid[:5].upper() == 'SANTO')