# Faca um programa que leia 10 inteiros positivos, ignorando nao positivos, e imprima sua
# media.

v = []
count = 0
for i in range(10):
    result = int(input('digite um valor: '))
    count += 1
    if result >= 0:
        v.append(result)
        print(v)
for num in v:
    x = (num + count) / 2
print(x)
        