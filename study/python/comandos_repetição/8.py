# Escreva um programa que leia 10 numeros e escreva o menor valor lido e o maior valor
# lido.

v = []
for i in range(10):
    result = input('digite um valor: ')
    v.append(result)
x = min(v)
y = max(v)
print(x)
print(y)