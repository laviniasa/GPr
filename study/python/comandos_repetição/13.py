# Faca um programa que leia um n  ́umero inteiro positivo par N e imprima todos os n  ́umeros
# pares de 0 at  ́e N em ordem crescente


v = []
n = int(input('digite um valor: '))

for num in range(0, n):
    if num % 2 == 0:
        v.append(num)
print(v)        