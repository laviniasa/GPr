#13.1
#  Ao receber 4 sequencias de números
# crie uma função que retorne uma matriz, 
# onde cada sequência é uma lista seja uma coluna, na ordem em que for recebida

def coll (seq1, seq2, seq3, seq4):
    matriz = []
    count = 0
    for i in seq1:
        subMatriz = []
        subMatriz.append(seq1[count])
        subMatriz.append(seq2[count])
        subMatriz.append(seq3[count])
        subMatriz.append(seq4[count])
        matriz.append(subMatriz)
        count = count + 1

    return matriz

arrey = [1,2,3,]
arrey2 = [6,7,8]
arrey3 = [5,0,4]
arrey4 = [9,0,1]    

test = coll(arrey, arrey2, arrey3, arrey4)

for linha in test:
        for lugar in linha:
            print(lugar, end=" - ")
        print("")

