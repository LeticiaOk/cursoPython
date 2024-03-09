"""
Crie um código em python que teste se o site Pudim
está acessível pelo computador usado.
"""

# from requests import get

# try:
#     get('https://pudim.com.br')
# except:
#     print('\033[31mO site Pudim não está acessível no momento.\033[m')
# else:
#     print('\033[32mConsegui acessar o site Pudim com sucesso!\033[m')

# RESOLUÇÃO
import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('O site Pudim não está acessível no momento.')
else:
    print('Consegui acessar o site Pudim com sucesso!')
    # print(site.read()) # mostra o HTML