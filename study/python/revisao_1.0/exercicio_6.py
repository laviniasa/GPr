# Leia uma matriz 10 x 10 e escreva a localização (linha e a coluna) do maior valor.

from random import randint

matriz_10x10 = []

for linha in range(10):
    linha = []

    for coluna in range(10):
        linha.append(randint(0, 10000))

    matriz_10x10.append(linha)

for linha_matriz in matriz_10x10:
    print(linha_matriz)

element = (0, )

for line in matriz_10x10:
    for value in line:
        if element[0] < value:
            x = line.index(value)
            y = matriz_10x10.index(line)
            element = (value, y, x)
print(element)