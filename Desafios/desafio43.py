peso = float(input("DIgite seu peso(em KG): "))
altura = float(input("Digite sua altura(em metros): "))

IMC = peso / (altura**2)

if IMC < 18.5:
    print("Você está ABAIXO do peso!")
elif IMC < 25:
    print("Você está com o peso IDEAL!")
elif IMC < 30:
    print("Você está com SOBREPESO!")
elif IMC < 35:
    print("Você está com OBESIDADE!")
else:
    print("Você está com OBESIDADE MÓRBIDA!")