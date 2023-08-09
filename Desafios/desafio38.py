num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))

if num1 > num2:
    print('O maior número é {}.'.format(num1))
elif num2 > num1:
    print('O maior número é {}.'.format(num2))
else:
    print('Os dois números tem o mesmo valor')