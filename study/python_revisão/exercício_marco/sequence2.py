# Uma função deve retornar uma lista com os números das duas sequências ordenada crescente

def ordenar(list1, list2):
    listResult = []
    listResult = list1+list2
    return sorted(listResult)

Seq1 = [1, 5, 9, 2]
Seq2 = [3, 4, 8, 6]

listOrdem = ordenar(Seq1, Seq2 )
print(listOrdem)