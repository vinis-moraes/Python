num = int(input("Digite um número: "))
divisores = 0
for c in range(1, num+1):
    if c == 1 or c == num:
        divisores += 1
    else:
        resto = num % c
        if resto == 0:
            divisores += 1
if divisores > 2:
    print("Não é primo!")
else:
    print("É primo!")