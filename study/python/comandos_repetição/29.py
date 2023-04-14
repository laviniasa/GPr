# Escreva um programa para calcular o valor da serie, para 5 termos.
# S = 0 + 1/2! + 2/4! + 3/6! + ...
f = 1
for i in range(5):
    n = int(input("Digite um número para calcular seu Fatorial;" ))
    c = n 
    while c > 0:
        print('{}'.format(c), end = '')
        print(' x ' if c > 1 else ' = ', end = '')
        f *= c 
        c -= 1
    print('{}'.format(f))
    print('Calculando {}! ='.format(n), end = '')
