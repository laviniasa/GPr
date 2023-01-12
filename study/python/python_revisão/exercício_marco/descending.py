#1.2 - Uma função deve retornar a sequência ordenada decrescente

#def orderly(n):
#    return n.sort()
    
#x = [2,3,1,9,7,6,5,4,8]
#o = orderly(x)
#numeros_ordenados=reversed(x)

def descending(n):
    n.sort()
    n2 = reversed(n)
    return list(n2)

num = [4,9,12,20,5,2,7]
print(descending(num))


