list = [
    int(input('Digite um valor: ')),
    int(input('Digite outro valor: ')),
    int(input('Digite mais um valor: ')),
    int(input('Digite mais um outro valor: ')),
    int(input('Digite o último valor: '))
]

menor = [0, 0]
maior = [0, 0]


for c in range(len(list)):
    if list[c] > maior[0] or maior[0] == 0:
        maior.pop()
        maior.pop()
        maior.insert(0, list[c])
        maior.insert(1, c)
 #   if list[c] < menor[0] or menor[0] == 0:
  #      menor[0] = list[c]
   #     menor[1] = c + 1


#print(f"Menor valor: {menor[0]} na posição {menor[1]}")
print(f"Maior valor: {maior[0]} na(s) posição(ões) {maior[1:]}")