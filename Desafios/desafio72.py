cont = ('zero', 'um', 'dois', 'três', 'quatro',
        'cinco', 'seis', 'sete', 'oito', 'nove',
        'dez', 'onze', 'doze', 'treze', 'catorze',
        'quinze', 'dezesseis', 'dezessete', 'dezoito',
        'dezenove', 'vinte')
n = -1
while True:
    while n < 0 or n > 20:
        n = int(input("Digite um número entre 0 e 20: "))
    break
print(f'Você digitou o número {cont[n]}')