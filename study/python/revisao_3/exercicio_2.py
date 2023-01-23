#Declare um vetor de 10 posições e o preencha com os 10 primeiros números impares e o escreva.

def recovering_i(n):
    v = []
    for i in n:
        if i % 2 != 0:
            v.append(i)
    return v

v = [1,2,3,4,5,6,7,8,9,10]

print(recovering_i(v))

