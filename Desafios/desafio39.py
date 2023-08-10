import datetime

today = datetime.date.today()

ano_atual = today.year

ano = int(input("Digite seu ano de nascimento: "))
idade = ano_atual - ano

if idade == 18:
    print("É a hora de se alistar!")
elif idade > 18:
    print("Já passou do tempo do alistamento!")
    print("Já se passaram {} anos desde o prazo.".format(idade - 18))
else:
    print("Você ainda vai se alistar!")
    print("Ainda faltam {} anos para o prazo!".format(18-idade))

