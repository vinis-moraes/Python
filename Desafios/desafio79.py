list = []
action = ""
while True:
    num = int(input("Digite um valor: "))
    if list.count(num) == 0:
        list.append(num)
        print("Número adicionado!")
    else:
        print("Número repetido, não adicionado!")
    while action != "S" and action != "N":
        action = str(input("Você deseja continuar? [S/N] "))
        action = action.upper()
    if action == "N":
        break
    action = ""
list.sort()
print(list)