over18 = 0
men = 0
womenu20 = 0
while True:
    idade = int(input("Digite a idade: "))
    sexo = "Nothing"
    while sexo != "H" and sexo != "M":
        sexo = str(input("Qual o sexo da pessoa? [H/M] "))
        sexo = sexo.upper()
    if idade > 18:
        over18 += 1
    if sexo == "H":
        men += 1
    if sexo == "M" and idade < 20:
        womenu20 += 1
    keep = "-"
    while keep != "S" and keep != "N":
        keep = str(input("Você deseja inserir mais dados? [S/N] "))
        keep = keep.upper()
    if keep == "N":
        break
print(f"{over18} pessoas têm mais de 18 anos.")
print(f"{men} homens foram cadastrados.")
print(f"{womenu20} mulheres com menos de 20 anos foram cadastradas.")