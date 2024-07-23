c = 0
sum = 0
list = 0
while c != 999:
    c = int(input("Digite um número: "))
    if c != 999:
        sum = sum + c
        list = list + 1

print("Você digitou {:.0f} números e a soma foi {:.0f}".format(list, sum))