from random import randint
playerchoice  = str("Nothing")
playerwinner = 0
while True:
    computer = randint(1,100)
    while playerchoice != "P" and playerchoice != "I":
        playerchoice = str(input("Deseja par ou ímpar? [P/I]"))
        playerchoice = playerchoice.upper()
    player = int(input("Digite um número: "))
    sum = computer + player
    result = sum % 2
    if playerchoice == "I" and result == 1 or playerchoice == "P" and result == 0:
        playerwinner += 1
        playerchoice = "Nothing"
    else:
        break

print(f'O jogo acabou! Você venceu em {playerwinner} rodadas.')

