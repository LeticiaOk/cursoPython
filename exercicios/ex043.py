# peso = float(input('Digite seu peso: '))
# altura = float(input('Digite sua altura: '))
# imc = peso/(altura*altura)

# print('IMC: {}'.format(imc))
# if imc < 18.5:
#     print('\033[34mAbaixo do peso\033[m')
# elif imc >= 18.5 and imc < 25:
#     print('\033[34mPeso ideal\033[m')
# elif imc >= 25 and imc < 30:
#     print('\033[34mSobrepeso\033[m')
# elif imc >= 30 and imc <= 40:
#     print('\033[34mObesidade\033[m')
# elif imc > 40:
#     print('\033[34mObesidade mórbida\033[m')

peso = float(input('Qual é o seu peso? (Kg) '))
altura = float(input('Qual é a sua altura? (m) '))
imc = peso/(altura ** 2)
print('O IMC dessa pessoa é de {:.1f}'.format(imc))

if imc < 18.5:
    print('Você está ABAIXO DO PESO normal')
elif  18.5 <= imc < 25:
    print('PARABÉNS, você está na faixa de PESO NORMAL')
elif 25 <= imc < 30:
    print('Você está em SOBREPESO')
elif 30 <= imc < 40:
    print('Você está em OBESIDADE!')
elif imc >= 40:
    print('Você está em OBESIDADE MÓRBIDA, cuidado!')