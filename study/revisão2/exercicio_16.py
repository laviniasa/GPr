# Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. 
# Ex.: 5!=5.4.3.2.1=120

def fatorial(n, show=False):
    f = 1
    for c in range(n, 0, -1):
        if show:
            print (c,end='')
            if c > 1: 
                print (' * ',end='')
            else:
                print(' = ', end='')
        f*=c
    return f

print(fatorial(5,show=True))

# a= 5
# test=fatorial(a)
# print(test)