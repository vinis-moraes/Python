pt = float(input("Digite o primeiro termo: "))
r = float(input("Digite a razão da PA: "))

s = pt
c = 10

while c > 0:
    s += r
    print(s)
    c = c - 1