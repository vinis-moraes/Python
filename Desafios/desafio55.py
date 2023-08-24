#!/usr/bin/env python3

menor_peso = 0
maior_peso = 0
for c in range(0,5):
	peso = float(input('Digite seu peso: '))
	if menor_peso == 0:
		menor_peso = peso
	elif menor_peso > peso:
		menor_peso = peso
	
	if maior_peso == 0:
		maior_peso = peso
	elif maior_peso < peso:
		maior_peso = peso
print('O menor peso foi {} kg'.format(menor_peso))

print('O maior peso foi {} kg'.format(maior_peso))