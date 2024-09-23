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
print(30*'-=')
print(f'Você digitou {len(list)} elementos.')
list.sort(reverse=True)
print(f'Os valores em ordem decrescente são {list}')
if list.count(5) == 0:
    print("O valor 5 não faz parte da lista!")
else:
    print("O valor 5 faz parte da lista!")