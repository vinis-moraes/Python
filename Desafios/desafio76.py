list = (
    str("Arroz"),
    int(10),
    str("Feijão"),
    int(15),
    str("Macarrão"),
    int(8),
    str("Coca-Cola"),
    int(10)
)

print("===== Listagem de preços =====")
print("Produtos" + 17*" " + "Preço")
for c in range(len(list)):
    if c % 2 == 0:
        print(f'{list[c] : <10} ' + f"{'-':^12}" + f"R${list[c+1]:>3},00")