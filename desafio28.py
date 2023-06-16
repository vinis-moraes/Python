import random

num = random.randint(0,5)

print('Pensei em um número entre 0 e 5...')
tentativa = int(input('Digite o número que você acha que eu pensei: '))

if tentativa == num:
    print('Acertou!')
else:
    print('Errou!')