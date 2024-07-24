list = (
    str("porta"),
    str('janela'),
    str('casa'),
    str('rua'),
    str('igreja'),
    str('asfalto')
)

for c in list:
    print(f"A palavra \"{c}\" possui as vogais: ", end="")
    for i in c:
        if i.lower() in 'aeiou':
            print(i, end=' ')
    print(end='\n')