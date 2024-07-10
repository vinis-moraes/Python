#!/usr/bin/env python3

v1 = float(input("Digite o primeiro valor: "))
v2 = float(input('Digite o segundo valor: '))

opcao = 0
while opcao != 5:
	print('''	[1] Somar
	[2] Multiplicar
	[3] Maior
	[4] Novos Números
	[5] Sair do programa''')
	opcao = int(input('Escolha a operação desejada: '))
	if opcao == 1:
		print("A soma dos valores é {:.0f}".format(v1+v2))
	elif opcao == 2:
		print("O produto dos valores é {:.0f}".format(v1*v2))
	elif opcao == 3:
		if v1 > v2:
			print("O valor {:.0f} é maior do que {:.0f}".format(v1, v2))
		elif v2 > v1:
			print("O valor {:.0f} é maior do que {:.0f}".format(v2, v1))
		else:
			print("Os valores são iguais")
	elif opcao == 4:
		v1 = float(input("Digite o primeiro valor: "))
		v2 = float(input('Digite o segundo valor: '))
	elif opcao == 5:
		print("Finalizando...")
	else:
		print("Digite uma opção válida")
print("Fim do programa!")
