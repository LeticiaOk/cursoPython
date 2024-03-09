# opcao = 0
# v1 = int(input('Digite o 1° valor: '))
# v2 = int(input('Digite o 2° valor: '))

# while opcao != 5:

#     opcao = int(input('Esolha a operação: \n[1] somar \n[2] multiplicar \n[3] maior \n[4] novos números \n[5] Sair do programa\nSua operação: '))
#     if opcao == 1:
#         print('{} + {} = {} '.format(v1, v2, v1 + v2))
#     elif opcao == 2:
#         print('{} x {} = {}'.format(v1,v2, v1*v2))
#     elif opcao == 3:
#         if v1 > v2:
#             print('O maior valor é: {}'.format(v1))
#         if v2 > v1:
#             print('O maior valor é: {}'.format(v2))
#     elif opcao == 4:
#        v1 = int(input('Digite o 1° valor: '))
#        v2 = int(input('Digite o 2° valor: '))
# print('Programa finalizado!')

from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundoo valor: '))
opcao = 0
while opcao != 5:

    print('''    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa ''')
    opcao = int(input('>>>>>Qual é a sua opção? '))
    if opcao == 1:
        soma = n1 + n2
        print('A soma entre {} + {} é {}'.format(n1, n2, soma))
    elif opcao == 2:
        produto = n1 * n2
        print('O resultado de {} x {} é {}'.format(n1,n2,produto))
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Entre {} e {} o maior valor é {}'.format(n1,n2, maior))
    elif opcao == 4:
        print('Informe os números novamente: ')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Swgundo valor: '))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente')
    print('=-=' * 10)
    sleep(2)
print('Fim do programa! Volte sempre')
