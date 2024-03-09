# mais18 = homens = mulheres20 = 0

# while True:
#     print('-' * 20)
#     print('\033[35mCADASTRE UMA PESSOA\033[m')
#     print('-' * 20)

#     sexo = opcao = ''
#     idade = 0

#     while idade <= 0:
#         idade = int(input('Idade: '))

#     while sexo != 'M' and sexo != 'F':
#         sexo = str(input('Sexo [M/F]: ')).upper().strip()

#     if idade >= 18:
#         mais18+=1

#     if sexo == 'M':
#         homens += 1
    
#     if idade < 20 and sexo  == 'F':
#         mulheres20 += 1

#     while opcao != 'S' and opcao != 'N':
#         opcao = str(input('Deseja cadastrar outra pessoa? [S/N]: ')).upper().strip()
    
#     if opcao == 'N':
#         break

# print(44 * '-')  
# print(f'Total de pessoas com mais de 18 anos: {mais18}')
# print(f'Total de homens cadastrados: {homens}')
# print(f'Total de mulheres com menos de 20 anos: {mulheres20}')
# print(44 * '-')

tot18 = totH = totM20 = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    
    if idade >= 18:
        tot18 += 1

    if sexo == 'M':
        totH += 1

    if sexo == 'F' and idade < 20:
        totM20 += 1

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    
    if resp == 'N':
        break
    
print(f'Total de pessoas com mais de 18 anos: {tot18}')
print(f'Ato todo temos {totH} cadastrados')
print(f'E temos {totM20} mulheres com menos de 20 anos')