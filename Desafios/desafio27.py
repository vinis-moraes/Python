nome = str(input('Digite seu nome completo: '))
print('Seu nome é {}'.format(nome))
dividido = nome.split()
ultimo = len(dividido)
print(ultimo)
print('O primeiro nome é {}'.format(dividido[0]))
print('O último nome é {}'.format(dividido[ultimo-1]))