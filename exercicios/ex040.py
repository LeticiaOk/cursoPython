# n1 = float(input('Digite sua primeira nota: '))
# n2 = float(input('Digite sua segunda nota: '))
# media = (n1 + n2)/2

# print('Sua média foi: {}'.format(media))
# if media < 5.0:
#     print('\033[31mREPROVADO\033[m')
# elif media >= 5.0 and media <= 6.9:
#     print('\033[33mRECUPERAÇÃO\033[m')
# elif media >= 7.0:
#     print('\033[32mAPROVADO\033[m')

nota1 = float(input('Primeira nora: '))
nota2 =float(input('Segunda nota: '))
media = (nota1 + nota2)/2
print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(nota1,nota2,media))
if 7 > media >= 5:
    print('O aluno está em RECUPERAÇÃO.')
elif media < 5:
    print('O aluno está REPROVADO.')
elif media >= 7:
    print('O aluno está APROVADO.')