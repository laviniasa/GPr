#2.4 - Uma função deve retornar uma lista com os números das
#  duas sequências ordenada decrescente

def ordenar(list1, list2):
    return sorted(list1+list2, key=int, reverse=True)

Seq1 = [1, 5, 9, 2]
Seq2 = [3, 4, 8, 6]

listOrdem = ordenar(Seq1, Seq2 )
print(listOrdem)