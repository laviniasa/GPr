# Uma função que retorne uma matriz, onde cada sequência é uma lista seja uma linha,
#  na ordem em que for recebida, adicionada de uma coluna que seja a soma das células de cada linha, 
# e uma linha que seja a soma das células de cada coluna.


def matriz(m, n):
    matriz = []
    for i in range(n):
        matriz.append([5]*m)
    for i in range(n):
        print(matriz[i])

n = 5
m = 5

test = matriz(n,m )
print(test)