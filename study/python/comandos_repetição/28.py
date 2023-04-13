#  Fac ̧ a um programa que leia um valor N inteiro e positivo, calcule o mostre o valor E,
# conforme a f  ́ormula a seguir
# E = 1 + 1/1! + 1/2! + 1/3! + ... + 1/N 


n = int(input("Digite um número para calcular seu Fatorial;" ))
c = n 
f = 1

print('Calculando {}! ='.format(n), end = '')
while c > 0:
    print('{}'.format(c), end = '')
    print(' x ' if c > 1 else ' = ', end = '')
    f *= c 
    c -= 1
print('{}'.format(f))