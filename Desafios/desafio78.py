list = []
for c in range(0,5):
    list.append(int(input(f'Digite o número para a posição {c}: ')))
    if c == 0:
        maior = menor = list[c]
    else:
        if list[c] > maior:
            maior = list[c]
        if list[c] < menor:
            menor = list[c]

print(f'O maior valor é {maior} na(s) posição(ões) ', end="")
for i, v in enumerate(list):
    if v == maior:
        print(f'{i} ', end="")
print("")
print(f'O menor valor é {menor} na(s) posição(ões) ', end="")
for i, v in enumerate(list):
    if v == menor:
        print(f'{i}', end=" ")
print("")