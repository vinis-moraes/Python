answer = "Y"
sum = 0 
list = 0
smaller = 0
bigger = 0


while answer == "Y":
    num = int(input("Digite um número: "))
    sum = sum + num
    list = list + 1
    if num < smaller or list == 1:
        smaller = num
    if num > bigger or list == 1:
        bigger = num
        
    answer = str(input("Você deseja adicionar outro número? [Y/N] "))
    answer = answer.upper()
    while answer != "Y" and answer != "N":
        print("Por favor, insira um valor válido")
        answer = str(input("Você deseja adicionar outro número? [Y/N] "))
        answer = answer.upper()

print("O maior número digitado foi {:.0f}".format(bigger))
print("O menor número digitado foi {:.0f}".format(smaller))
print("Foram digitados {:.0f} números".format(list))
avrg = sum / list
print("A média dos números digitados foi {:.2f}".format(avrg))