vel = float(input('Digite a velocidade do carro(em km/h): '))

if vel > 80:
    vezes = vel - 80
    multa = vezes * 7
    print('Você foi MULTADO! Sua multa é de R${:.2f}'.format(multa))
else:
    print('Tudo certo!')