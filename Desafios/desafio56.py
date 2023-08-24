#!/usr/bin/env python3

soma = 0
mais_velho_idade = 0
mais_velho = 0
menos_vinte = 0
for c in range(0,4):
	nome = str(input('Digite o nome: '))
	idade = int(input("Digite sua idade: "))
	sexo = int(input("Qual o seu sexo (1 = masculino, 2 = feminino): "))
	
	soma += idade
	
	if sexo == 1 and idade > mais_velho_idade:
		mais_velho = nome
		mais_velho_idade = idade
	
	if sexo == 2 and idade < 20:
		menos_vinte += 1
		
media = soma / 4
		
print('A média da idade do grupo é de {} anos.'.format(media))
print('O nome do homem mais velho é {}.'.format(mais_velho))
print("{} mulheres têm menos de 20 anos.".format(menos_vinte))