list = [[], []]
temp = int
for c in range(1,8):
    temp = (int(input(f'Digite o {c}º valor: ')))
    if temp % 2 == 0:
        list[0].append(temp)
    else:
        list[1].append(temp)
list[0].sort()
list[1].sort()
print(f'Os valores pares foram {list[0]}')
print(f'Os valores ímpares foram {list[1]}')