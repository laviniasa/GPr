#3.2
#  Ao receber 4 sequencias de números
#crie uma função que retorne uma matriz
# onde cada sequência é uma lista seja uma linha, na ordem em que for recebida

def matriz (seq1, seq2, seq3, seq4):

    matriz= []  
    matriz.append(seq1)
    matriz.append(seq2)
    matriz.append(seq3)
    matriz.append(seq4)
    return matriz

arrey = [1,2,3]
arrey2 = [6,7,8]
arrey3 = [5,0,4]
arrey4 = [9,0,1]    

test = matriz(arrey, arrey2, arrey3, arrey4)
print(test)

