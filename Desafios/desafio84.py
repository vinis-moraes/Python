list = []
temp = []
action = ""
while True:
    temp.append(str(input("Nome: ")))
    temp.append(int(input("Peso: ")))
    list.append(temp[:])
    temp.clear()
    while action != "S" and action != "N":
        action = str(input("Quer continuar? [S/N] "))
        action = action.upper()
    if action == "N":
        break
    action = ""
print(30 * "-=")
pesado = int
leve = int
npesado = []
nleve = []
for c in range(len(list)):
    if c == 0 or list[c][1] > pesado:
        pesado = list[c][1]
        npesado.clear()
        npesado.append(list[c][0])
    elif list[c][1] == pesado:
        npesado.append(list[c][0])
    if c == 0 or list[c][1] < leve:
        leve = list[c][1]
        nleve.clear()
        nleve.append(list[c][0])
    elif list[c][1] == leve:
        nleve.append(list[c][0])
print(f'Ao todo, você cadastrou {len(list)} pessoas.')
print(f'O maior peso foi de {pesado:.2f}Kg. Peso de {npesado}')
print(f'O menor peso foi de {leve:.2f}Kg. Peso de {nleve}')