km = int(input('Digite a distância da viagem: '))

if km <= 200:
    preco = km * 0.5
    print('A passagem custará R${:.2f}'.format(preco))
else:
    preco = km * 0.45
    print('A passagem custará R${:.2f}'.format(preco))