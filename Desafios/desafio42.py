r1 = float(input("Digite o tamanho da primeira reta: "))
r2 = float(input("Digite o tamanho da segunda reta: "))
r3 = float(input("Digite o tamanho da terceira reta: "))

if r1 + r2 > r3 and r2 + r3 > r1 and r3 + r1 > r2:
    print("Você pode formar um triângulo")
    if r1 == r2 and r1 == r3:
        print("Esse triângulo será EQUILÁTERO!")
    elif r1 == r2 or r2 == r3 or r3 == r1:
        print("Esse triângulo será ISÓSCELES!")
    else:
        print("Esse triângulo será ESCALENO!")
else:
    print("Você não pode formar um triângulo")