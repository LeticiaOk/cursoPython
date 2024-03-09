
# valores = (int(input(f'Digite o 1° valor: ')), int(input(f'Digite o 2° valor: ')), int(input(f'Digite o 3° valor: ')), int(input(f'Digite o 4° valor: ')))
     
# print(valores)
# if 9 in valores:
#     print(f'O valor 9 apareceu {valores.count(9)} vezes')
# else:
#     print('O valor 9 não apareceu nenhuma vez')
# if 3 in valores:
#     print(f'O valor 3 foi digitado na {valores.index(3) + 1}° posição')
# else:
#     print('O valor 3 não foi digitado em nenhuma posição')

# print('Os valores pares digitados foram:',end=' ')
# for n in valores:
#     if n % 2 == 0:
#         print (n, end=' ')




# if valores % 2 == 0: # não funciona
#     print (valores)
# print('Os números pares digitados foram')



# for c in range (1,5):
#     valor = int(input(f'Digite o {c}° valor: '))
#     valores += (valor,)
  
# print(valores)
# if 9 in valores:
#     print(valores.count(9))
# else:
#     print('O valor 9 não apareceu nenhuma vez')
# if 3 in valores:
#     print(valores.index(3))
# else:
#     print('O valor 3 não foi digitado em nenhuma posição')



num  = (int(input('Digite um número: ', )),
        int(input('Digite outro número: ', )),
        int(input('Digite mais um número: ', )),
        int(input('Digite o último número: ', )))
print(f'Você digitou os valores: {num}')
print(f'O valor 9 apareceu {num.count(9)} vezes')

if 3 in num:
    print(f'O valor 3 apareceu na {num.index(3) + 1}ª posição')
else:
    print('O valor 3 não foi digiato em nenhuma posição')
print('Os valores pares digitados foram ', end='')

for n in num:
    if n % 2 == 0:
        print(n, end=' ')