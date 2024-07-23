while True:
    num = int(input('Digite o valor: '))
    if num < 0:
        break
    c = 0
    while c <= 10:
        print  (f'{c} x {num} = {c*num}')
        c +=1