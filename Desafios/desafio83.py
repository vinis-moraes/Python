expressao = str(input("Digite uma expressão: "))
i = 0
for c in range(len(expressao)):
    if expressao[c] == "(":
        i += 1
    if expressao[c] == ")":
        i -= 1
if i == 0:
    print("Expressão válida")
else:
    print("Expressão inválida")