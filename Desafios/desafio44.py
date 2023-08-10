valor_normal = float(input("Digite o valor do produto: R$ "))
print("Opções de pagamento:")
print("[1] À vista (dinheiro ou cheque)")
print("[2] À vista no cartão")
print("[3] Até 2x no cartão")
print("[4] 3x ou mais no cartão")
modo = int(input("Selecione a opção desejada (1-4): "))
if modo < 1 or modo > 4:
    print("Por favor, selecione uma opção válida!")
    modo = int(input("Selecione a opção desejada (1-4): "))

if modo == 1:
    print("O valor a pagar é de R$ {:.2f}".format(valor_normal-(valor_normal/10)))
elif modo == 2:
    print("O valor a pagar é de R$ {:.2f}".format(valor_normal-(valor_normal/20)))
elif modo == 3:
    print("O valor a pagar é de R$ {:.2f}".format(valor_normal))
else:
    print("O valor a pagar é de R$ {:.2f}".format(valor_normal+(valor_normal/5)))