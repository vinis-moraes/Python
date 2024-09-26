list = [[0,0,0],[0,0,0], [0,0,0]]
num = int
for l in range(0,3):
    for c in range(0,3):
        list[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))

for l in range(0,3):
    for c in range(0,3):
        print(f'[{list[l][c]:^5}]', end="")
    print("")