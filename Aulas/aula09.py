frase = 'Curso em Vídeo Python'
print(frase)
print(frase[3])
print(frase[3:13])
print(frase[:13])
print(frase[13:])
print(frase[1:15])
print(frase[3:15:2])
print(frase[3::2])
print(frase[::2])

print('Oi')

print("""       Lorem ipsum dolor sit amet consectetur adipisicing elit.
    Temporibus voluptatum qui incidunt exercitationem nulla dicta quae
    reiciendis, cupiditate facere assumenda laboriosam tempore quos,
    eos expedita aspernatur animi inventore tenetur. Molestias?""")

print(frase.count('o'))
print(frase.upper().count('O'))
print(len(frase))
print(frase.replace('Python', 'Android'))
print(frase)
print('Curso' in frase)
print(frase.find('Curso'))
print(frase.find('Vídeo'))
print(frase.find('vídeo'))
print(frase.lower().find('vídeo'))

dividido = frase.split()
print(dividido)
print(dividido[0])
print(dividido[2])
print(dividido[2][3])