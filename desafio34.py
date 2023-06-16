salario = float(input('Digite o seu salário: '))

if salario > 1250.00:
    novo = salario + (salario/10)
    print('Seu novo salário é de R${:.2f}'.format(novo))
else:
    novo = salario + (salario/20*3)
    print('Seu novo salário é de R${:.2f}'.format(novo))