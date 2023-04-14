# Fac ̧ a um programa que leia um n  ́umero inteiro positivo N e imprima todos os n  ́umeros
# naturais de 0 at  ́e N em ordem decrescente.

v = []

n = int(input('digite um valor: '))

for num in range(0, n):
    v.append(num)
v = v.reverse()
for x in v:
    print(x)
    