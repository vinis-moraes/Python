#!/usr/bin/env python3
import datetime

ano_atual = datetime.date.today().year
print(ano_atual)

maior = 0
menor = 0

for c in range(0,7):
	ano = int(input('Digite seu ano de nascimento: '))
	idade = ano_atual - ano
	if idade > 18:
		maior += 1
	else:
		menor += 1
print('{} pessoas são maiores de idade e {} pessoas são menores de idade' .format(maior, menor))
