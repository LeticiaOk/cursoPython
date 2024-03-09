
def leiaDinheiro(num):
    
    while num.strip() == '' or num.isdigit() == False:
        num = input('Digite o preço: R$').strip()

        valid = ''
        novo = ''
        for i in num:
            if i != ',' and i  != '.':
                valid += i

        if valid.isdigit():
            for i in num:
                if i == ',' or i == '.':
                    novo+='.'
                else:
                    novo += i
            novo = float(novo)
            
            break

        print(f'\033[31mERRO: "{num}" é um preço inválido!\033[m')
    return novo































    # while num.strip() == '' or num.isdigit() == False:
    #     num = input('Digite o preço: R$').strip()

# n = '850,99'
# novo = ''
# for i in n:
#     if i == ',':
#         novo+= '.'
#     else:
#         novo+= i
# print(novo.isdigit())
# novo = float(novo)
# print(novo)
# n = '8 5'
# print(n.isdigit())