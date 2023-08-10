import random
computer = random.randint(1,3)

print("SEJA BEM VINDO AO JOKEMPO!")
print("Escolha uma jogada:")
print("[1] Pedra")
print("[2] Papel")
print("[3] Tesoura")
jogada = int(input("Digite sua jogada (1-3): "))

if jogada == computer:
    print("O resultado foi EMPATE!")
elif jogada == 1 and computer == 2 or jogada == 2 and computer == 3 or jogada == 3 and computer == 1:
    print("O ganhador foi COMPUTADOR!")
else:
    print("O ganhador foi USUÁRIO")
