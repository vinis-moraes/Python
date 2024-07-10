num = int(input("Digite o número: "))

c = num
fatorial = num

while c > 1:
    c = c - 1
    fatorial = fatorial * c
print("O fatorial de {:.0f} é {:.0f}".format(num, fatorial))