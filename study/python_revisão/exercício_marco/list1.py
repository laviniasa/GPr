#2 - Ao receber duas sequência de números:
#2.1 - Uma função deve retornar, se for possível, a soma dos números como o exemplo a seguir:


def soma(list1, list2):
    listResult = []
    cont = 0
    for num in list1:
        listResult.append(list1[cont]+list2[cont])
        cont = cont + 1
    return listResult

Seq1 = [1, 5, 9, 2]
Seq2 = [5, 10, 4, 9]

somar = soma(Seq1, Seq2 )
print(somar)
