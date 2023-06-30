valor_casa = float(input('Digite o valor da casa: R$ '))
valor_sal = float(input('Digite o salário do comprador: R$ '))
anos = int(input('Digite em quantos anos a casa será paga: '))


mensal = valor_casa / (anos*12)

razao = mensal / valor_sal

print(razao)

if razao > 0.3:
    print('EMPRÉSTIMO NEGADO')
else:
    print('EMPRÉSTIMO AUTORIZADO')