#1.2 - Uma função deve retornar a sequência ordenada decrescente

def descending(n):
    n.sort()
    n2 = reversed(n)
    return list(n2)

num = [4,9,12,20,5,2,7]
test = descending(num)
print(test)