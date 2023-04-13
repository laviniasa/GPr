# Faca um programa que leia um n  ́umero inteiro positivo par N e imprima todos os n  ́umeros
# pares de 0 ate N em ordem decrescente

v = []
n = int(input('digite um valor: '))

for num in range(0, n):
    if num % 2 == 0:
        v.append(num)
v.reverse()    
print(v)
