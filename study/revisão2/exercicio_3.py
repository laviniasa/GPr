# Uma função deve retornar uma lista com os números das duas 
# sequências ordenada crescente

def order(list1, list2):
    listResult = list1+list2
    return sorted(listResult)

Seq1 = [1, 5, 9, 2]
Seq2 = [3, 4, 8, 6]

listOrder = order(Seq1, Seq2)
print(listOrder)