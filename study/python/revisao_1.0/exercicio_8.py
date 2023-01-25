#Leia uma matriz 6 x 6,
#  conte e escreva quantos valores maiores que 10 ela possui.

from random import randint

def maiores(n):
    v = []
    i = 0
    j = 0
    for linha in n:
        for coluna in linha:
            if (n[i][j] > 10):
                v.append (n[i][j])
                i += 1
                j += 1
    return v

matriz_6x6 = []

for linha in range(6):
    linha = []

    for coluna in range(6):
        linha.append(randint(0, 90))
    matriz_6x6.append(linha)

test = maiores(matriz_6x6)
print(test)
