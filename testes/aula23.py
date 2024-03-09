# TRATAMENTO DE ERROS E EXCEÇÕES

#try:
    #operação

#except:
    #falhou

#else:
    #deu certo

#finally:
    #certo/falha
    # aparece independente se deu certo ou falhou

#----------------------------------------------------
# EX1

# try:
#     a = int(input('Numerador: '))
#     b = int(input('Denominador: '))
#     r = a / b
# except Exception as erro:
#     print(f'Problema encontrado foi {erro.__class__}')
# else:
#     print(f'O resultado é {r:.1f}')
# finally:
#     print('Volte sempre! Muito obrigado!')

#------------------------------------------------------
# EX 2
    
# Um try pode ter varios except:
    
#try:
    #operação

#except TypeError:
    #falhou

#except ValueError:
    #falhou

#except OSEerror:
    #falhou

#else:
    #deu certo

#finally:
    #certo/falha
    # aparece independente se deu certo ou falhou

try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados que você digitou.')
except ZeroDivisionError:
    print(f'Não é possível dividir um número por zero!')
except KeyboardInterrupt:
    print('O usuário preferiu não informar os dados!')
except Exception as erro:
    print(f'O erro encontrado foi {erro.__cause__}')
else:
    print(f'O resultado é {r:.1f}')
finally:
    print('Volte sempre! Muito obrigado!')