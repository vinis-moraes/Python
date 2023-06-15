frase = str(input('Digite uma frase: '))
print('A letra "A" aparece {} vezes na frase.'.format(frase.count('A')))
print('A primeira vez que "A" aparece é na {}ª posição.'.format(frase.find('A')))
print('A última vez que "A" aparece é na {}ª posição.'.format(frase.rfind('A')))