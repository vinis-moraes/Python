pt = float(input("Digite o primeiro termo: "))
r = float(input("Digite a razão da PA: "))

s = pt
c = 10

while c > 0:
    s += r
    print("{:.0f}".format(s))
    c = c - 1

new = 0

new = int(input("Digite quantos termos você deseja ver a mais: "))
c = new
while c > 0:
    s += r
    print("{:.0f}".format(s))
    c = c - 1
    if c == 0:
        new = int(input("Digite quantos termos você deseja ver a mais: "))
        if new == 0:
            print("Saindo...")
            exit
        else:
            c = new