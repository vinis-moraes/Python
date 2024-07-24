nlist = (int(input("Digite um número: ")),
       int(input("Digite outro número: ")),
       int(input('Digite mais um número: ')),
       int(input('Digite o último número:')))
print(f"Os números digitados foram: {nlist}")
print(f"O valor 9 apareceu {nlist.count(9)} vezes")
print(f"O primeiro valor 3 foi digitado na {nlist.index(3)}ª posição")
print('Os valores pares digitados foram: ', end='')
for c in nlist:
    if c % 2 == 0:
        print(c,end=' ')
print(end='\n')