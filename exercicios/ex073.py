# times = ('Botafogo', 'Bragantino', 'Palmeiras', 'Flamengo', 'Athletico-PR', 'Grêmio', 'Atlético-MG', 'Fluminense','Fortaleza', 'São Paulo', 'Cuiabá', 'Cruzeiro', 'Corinthians', 'Internacional', 'Bahia','Goiás', 'Vasco da Gama', 'Santos', 'Coritiba', 'América-MG')
# print('\033[33mTIMES:\033[m')

# print(times)


# print('\n\033[32m5 PRIMEIROS COLOCADOS:\033[m')

# print(times[:5])


# print('\n\033[31mÚLTIMOS 4 COLOCADOS:\033[m')

# print(times[-4:])


# print('\n\033[34mTIMES POR ORDEM ALFABÉTICA:\033[m')

# print(sorted(times))


# for posicao in range(0, len(times)):
#     if times[posicao] == 'Corinthians':
#         print(f'\n\033[35mCorinthians está na {posicao + 1}° posição\033[m')

times = ('Botafogo', 'Bragantino', 'Palmeiras', 'Flamengo',
        'Athletico-PR', 'Grêmio', 'Atlético-MG', 'Fluminense',
        'Fortaleza', 'São Paulo', 'Cuiabá', 'Cruzeiro',
        'Corinthians', 'Internacional', 'Bahia','Goiás',
        'Vasco da Gama', 'Santos', 'Coritiba', 'América-MG') # Respeitar limite de 80 caracteres

print('-=' * 15)
print(f'Lista de times do Brasileirão: {times}')
# for t in times: 
#     print(t) # Faz aparecer os times um embaixo do outro
print('-=' * 15)
print(f'Os 5 primeiros são {times[0:5]}')
print('-=' * 15)
print(f'Os 4 últimos são {times[-4:]}')
print('-=' * 15)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-=' * 15)
print(f'O Chapecoense está na {times.index("Corinthians")+1}º posição') # Usar aspas duplas pois da erro no código se estiver dentro das aspaas da f string