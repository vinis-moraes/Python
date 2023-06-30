nome = str(input('Digite o nome completo de uma pessoa: '))

print('O nome é: {} (maiúsculas) ou {} (minúsculas)'.format(nome.upper(), nome.lower()))
print('O nome tem {} letras'.format(len(nome)-nome.count(" ")))
dividido = nome.split()
print('O primeiro nome tem {} letras' .format(len(dividido[0])))