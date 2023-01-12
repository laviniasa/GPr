#crie um programa que cria uma matriz n x m preenchida com zeros 

def matriz(n, m):
    matriz = []
    for i in range(n):
        matriz.append([0]*m)
    for i in range(n):
        print(matriz[i])
    
n = int(input('Digite a dimensão n da matriz: '))
m = int(input('Digite a dimensão m da matriz: '))

test = matriz(n,m )
print(test)