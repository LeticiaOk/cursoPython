
#EXEMPLO SEM LISTA
# expressao = str(input('Digite a expressão: '))

# abre = 0
# fecha = 0
# for c in range(0, len(expressao)):
#     print(expressao[c])
#     if expressao[c] == '(':
#         abre+=1
#     elif expressao[c] == ')':
#         fecha+=1
# if abre == fecha:
#     print('Expressão válida')
# else:
#     print('Expressão inválida!')



#EXEMPLOS DETALHADO COM LISTA
# lista = []
# expressao = str(input('Digite a expressão: '))
# abre = 0
# fecha = 0
# for c in range(0, len(expressao)):
#     lista.append(expressao[c])
#     print(lista[c])
#     if lista[c] == '(':
#         abre+=1
#     elif lista[c] == ')':
#         fecha+=1
# if abre == fecha:
#     print('Expressão válida')
# else:
#     print('Expressão inválida!')

# print(lista)
# print(len(lista))



#EXEMPLO MENOS DETALHADO COM LISTA
lista = []
expressao = str(input('Digite a expressão: '))

abre = 0
fecha = 0
for c in range(0, len(expressao)):
    lista.append(expressao[c])
    if lista[c] == '(':
        abre+=1
    elif lista[c] == ')':
        fecha+=1
if abre == fecha:
    print('Expressão válida')
else:
    print('Expressão inválida!')



# Outra maniera de percorrer cada elemento na string
# expressao = []
# expressao.append(str(input('Expressão: ')))
# for palavra in expressao:
#     # Iterando sobre cada letra na string atual
#     for letra in palavra:
#         print(letra)


expr = str(input('Digite a expressão: '))
pilha = []

for simb in expr:
    if simb == '(':
        pilha.append('(') #adiciona um parenteses aberto na lista
    elif simb == ')': # se o simbolo for parenteses fechando
        if len(pilha) > 0: # se os itens da lista for maior que 0
            pilha.pop() #remove o ultimo item da lista ou seja o parenteses abrindo
        else:
            pilha.append(')') # se o simbolo for parenteses fechando e a lista estiver vazia ou seja sem nenhum parenteses abrindo então adicona um aprenteses fechando(que é o simbolo atutal) dando expressão inválida pois apenas tem um parenteses fechando na pilha 
            break
if len(pilha) == 0:
    print('Sua expressão está valida!')
else:
    print('Sua expressão está inválida!')