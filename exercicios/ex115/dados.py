"""
Crie um pequeno sistema modularizado que permita
cadastrar pessoas pelo seu nome e idade em um arquivo
de texto simples.

O sistema vai ter 2 opções: cadastrar uma nova pessoa
e listar todas as pessoas cadastradas
"""
def titulo(msg):
    print('-' * 40)
    print(msg.center(40))
    print('-' * 40)

def sistema():
    dados = {}
    ficha = []
    while True:
        titulo('MENU PRINCIPAL')

        print('\033[33m1\033[m - \033[34mVer pessoas cadastradas\033[m')
        print('\033[33m2\033[m - \033[34mCadastrar nova pessoa\033[m')
        print('\033[33m3\033[m - \033[34mSair do sistema\033[m')

        print('-' * 40)

        while True:
            try:
                resp = int(input('\033[32mSua opção: \033[m'))
            except ValueError:
                print('\033[31mERRO! Digite um número inteiro válido!\033[m')
            else:
                if resp < 1 or resp > 3:
                    print('\033[31mERRO! Digite uma opção válida!\033[m')
                else:
                    break

        # OPÇÃO 1 DO MENU
        if resp == 1:
            titulo('PESSOAS CADASTRADAS')
            for p in ficha:
                print(f'{p["nome"]:30} \t{p["idade"]} anos')


        # OPÇÃO 2 DO MENU
        elif resp == 2:
            nome = ''
            idade = ''
            while True:
                try:
                    nome = str(input('Nome: '))
                    nomet = nome.strip().replace(" ", "")
                    if nomet.isalpha() == False:
                        nome = ''
                        print('\033[31mERRO! Digite caracteres válidos!\033[m')
                    else:
                        break
                except KeyboardInterrupt:
                     print('\033[35m\nNão foi possível concluir o cadastro\033[m')
                     break
                
            if nome.strip() != "":
                while True:
                    try:
                        idade = int(input('Idade: '))
                    except ValueError:
                        idade = ''
                        print('\033[31mERRO! Digite um número inteiro válido!\033[m')
                    except KeyboardInterrupt:
                        print('\033[35m\nNão foi possível concluir o cadastro\033[m')
                        break
                    else:
                        dados['nome'] = nome
                        dados['idade'] = idade
                        ficha.append(dados.copy())

                        print(f'Novo registro de {dados["nome"]} adicionado.')
                        break                   
        

        # OPÇÃO 3 DO MENU
        else:
            titulo('Saindo do sistema..Até logo!')
            break

sistema()

