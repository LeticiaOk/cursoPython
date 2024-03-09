# 20 caracteres       
frase = 'Curso em Vídeo Python'
#Fatiamento
print(frase[9]) # Mostra a o caractere 9
print(frase[9:13]) # Mostra do caractere 9 até o 12
print(frase[9:21]) # Mostra do caractere 9 até o 20
print(frase[9:21:2]) # Mostra do caractere 9 até o 20, pulando de 2 em dois
print(frase[:15]) # Mostra do  caractere 0 até o 5
print(frase[15:]) # Mostra do caractere 15 até o final
print(frase[9::3]) # Começa do caractere 9 até o final pulando de 3 em 3



#Análise
print(len(frase)) # Mostra quantos caracteres tem
print(frase.count('o')) # Mostra quantos 'o' tem
print(frase.count('o',0,13)) # Mostra quantos 'o' tem do caractrere 0 até o 12
print(frase.find('deo')) # Mostra em que momento começou o 'deo'
print(frase.find('Android')) # Mostra se tem a string dentro da frase se não tiver retorna -1
print('Curso' in frase) # Mostra se tem astring dentro da frase retornando true ou false




#Transformação
print(frase.replace('Python', 'Android')) # Substitui uma palavra pela outra
print(frase.upper()) # Substitui os caracteres minusculos por maisculos
print(frase.lower()) # Substitui os caracteres minusculos em maiusculos
print(frase.capitalize()) # Deixa apenas o primeiro caractre da string em maisculos e o resto em minusculo
print(frase.title()) # Deixa cada letra de cada palavra da string em maiusculo

frase2 = '   Aprendendo Python  '
print(frase2.strip()) # Remove todos os espaços inuteis no começo e no fim da string (o 'A' passa a ser o 0)
print(frase2.rstrip()) # Remove os espaços inuteis do lado direito
print(frase2.lstrip()) # Remove os espaços inuteis do lado esquerdo




#Divisão
print(frase.split()) # Ocorre uma divisão dentro da string considerando os espaços e cad divisão começa em 0 e cada uma das palacras é colocada dentro de uma nova lista começando do 0



#Junção
print('-'.join(frase)) # Considerando o split junta os elemento de frase (4) usando o separador '-'



#Testes
frase = 'Curso em Vídeo Python'
print(frase.upper().count('O')) # Transformou em maisusculos e depois contou os 'O' maiusculos

print(len(frase.strip())) # Leu a frase e pagaou os espaços

frase = frase.replace('Python' , 'Android')
print(frase) # Transformou a string
print(frase.lower().find('vídeo')) # Transfomoou em minuscula e mostrou onde começa a string

frase = 'Curso em Vídeo'
dividido = (frase.split())
print(dividido[0]) # Mostrou o primeiro item da lista

frase = 'Curso em Vídeo'
dividido = (frase.split())
print(dividido[2][3]) # Mostrou o caractere 3 do item 2 que é video

# print('Oi')

# print("""Ao clicar em «Aceito», concorda que nós e os nossos parceiros podemos armazenar e/ou aceder a informações no seu dispositivo,
# tais como IDs únicos em cookies para processar dados pessoais.
# Pode aceitar ou gerir as suas escolhas clicando abaixo, incluindo o seu direito de objeção sempre que seja utilizado um interesse legítimo.
# Pode retirar o seu consentimento ou gerir as suas escolhas em qualquer altura nas suas definições ou no gestor de cookies.end
# Para mais informações, consulte a nossa Política de Privacidade. As suas escolhas serão assinaladas aos nossos parceiros e não afetarão os dados de navegação.""")