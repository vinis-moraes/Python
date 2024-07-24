from random import randint

n1 = randint(0, 100)
n2 = randint(0, 100)
n3 = randint(0, 100)
n4 = randint(0, 100)
n5 = randint(0, 100)

listagem = (n1, n2, n3, n4, n5)
print(listagem)


menor = 0
maior = 0
for c in listagem:
    if c > maior or maior == 0:
        maior = c
    if c < menor or menor == 0:
        menor = c
print(f'Menor número: {menor}')
print(f'Maior número:{maior}')