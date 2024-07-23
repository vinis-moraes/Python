valor = int(input("Digite o valor: R$ "))
while True:
    if valor > 50:
        fifty = valor // 50
        valor = valor - (fifty * 50)
    if valor > 20:
        twenty = valor // 20
        valor = valor - (twenty * 20)
    if valor > 10:
        ten = valor // 10
        valor = valor - (ten * 10)
    if valor > 1:
        one = valor // 1
    break
print(f"Cédulas de R$ 50: {fifty}")
print(f"Cédulas de R$ 20: {twenty}")
print(f"Cédulas de R$ 10: {ten}")
print(f"Cédulas de R$ 1: {one}")