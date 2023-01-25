#1-Declare uma matriz 5 x 5. 
# 2-func-Preencha com 1 a diagonal principal e com 0 os demais elementos.
# 3-Escreva ao final a matriz obtida.
import numpy 

def diagonal(n):
    i = 0 
    j = 0
    for linha in n:
        for coluna in linha:
            n[i][j] = 1
            i += 1
            j += 1

    return n 
#1
matriz = numpy.zeros((5, 5)) 
for i in range(5): 
    for j in range(5): 
        matriz[i][j] = 0

#print(matriz)

print (diagonal(matriz))

# range é uma função que retorna os valores sequenciais, entre o intervalo informado.