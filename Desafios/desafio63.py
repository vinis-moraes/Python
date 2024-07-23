n = int(input("Digite a quantidade de números a serem calculados: "))

'''

Sequência de Fibonacci:

Fn = F(n - 1) + F(n - 2)

F(x) = F(x-1) + F(x-2)

Número: 10
c = 0
Fo = 1
Ft = 1
Fmo = 1
Fmt = 1
Enquanto c < Número (10):
    Se c == 0:
        F(c) = 0
    Se então c == 1 ou c == 2:
        F(c) = 1
    Senão:
        F(c)  = Fmo + Fmt
        Fmo = F(c)
        Fmt = F(c) - 1

'''
c = 0
Fo = 1
Ft = 1
Fmo = 1
Fmt = 1
Fc = 0

while c < n:
    if c == 0:
        Fc = 0 
        print(Fc)
        c = c + 1
    elif c == 1 or c == 2:
        Fc = 1
        print(Fc)
        c = c + 1
    else:
        Fc = Fmo + Fmt
        Fmt = Fmo
        Fmo = Fc
        print(Fc)
        c = c + 1