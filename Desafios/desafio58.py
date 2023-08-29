#!/usr/bin/env python3

import random

num = random.randint(0, 10)
jogada = 11
quantidade = 0
while jogada != num:
	print('Pensei em um número entre 0 e 10...')
	jogada = int(input("Digite o número que você acha que eu pensei: "))
	quantidade += 1
print('Parabéns! Você acertou com {} jogadas.'.format(quantidade))