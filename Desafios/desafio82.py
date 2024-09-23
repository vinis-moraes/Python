list = []
action = ""
while True:
    num = int(input("Digite um valor: "))
    if list.count(num) == 0:
        list.append(num)
    while action != "S" and action != "N":
        action = str(input("Quer continuar? [S/N] "))
        action = action.upper()
    if action == "N":
        break
    action = ""

print(30*"-=")
impar = []
par = []
for c in range(len(list)):
    if list[c] % 2 == 1:
        impar.append(list[c])
    else:
        par.append(list[c])

print(f'A lista completa é {list}')
print(f'A lista de números pares é {par}')
print(f'A lista de números ímpares é {impar}')
