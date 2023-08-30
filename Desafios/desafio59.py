#!/usr/bin/env python3

v1 = float(input("Digite o primeiro valor: "))
v2 = float(input('Digite o segundo valor: '))

opcao = 0
while opcao < 1 or opcao > 5:
	print("[1] Somar")
	print("[2] Multiplicar")
	print("[3] Maior")
	print("[4] Novos números")
	print("[5] Sair")
	
	
	opcao = int(input('Escolha a operação desejada: '))
if opcao == 1:
	print('O resultado da operação de SOMA é {}'.format(v1 + v2))
elif opcao == 2:
	print('O resultado da operação de MULTIPLICAÇÃO é {}'.format(v1 * v2))


