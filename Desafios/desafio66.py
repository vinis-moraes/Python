list = 0
sum = 0
while True:
    num = int(input("Digite o número: "))
    if num == 999:
        break
    list += 1
    sum += num
print(f'O valor da soma foi {sum} e a quantidade de números digitados foi {list}')