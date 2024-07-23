cheapest = "None"
cheapestp = 0.00
sum = 0.00
mtt = 0

while True:
    name = str(input("Nome do produto: "))
    price = float(input("Preço do produto: R$ "))
    if price > 1000:
        mtt += 1
    if cheapestp == 0.00 or price < cheapestp:
        cheapestp = price
        cheapest = name
    sum += price
    keep = "-"
    while keep != "S" and keep != "N":
        keep = str(input("Continuar adicionando produtos? [S/N] "))
        keep = keep.upper()
    if keep == "N":
            break
print(f"Total: R$ {sum:.2f}")
print(f"Produtos custando mais de R$ 1000,00: {mtt}")
print(f"O produto mais barato foi {cheapest}, custando R$ {cheapestp:.2f}")