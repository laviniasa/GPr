#1.3 - Uma função deve retornar o resultado da multiplicação dos dois maiores números
#Len () é uma função integrada ao Python que é utilizada para obter o número de itens em um determinado objeto, string, array, listas, entre outros.

def multiplication(list1): 
    l = len(list1) 
    #list1.sort() 
    return (list1[l-2])*(list1[l-1])
    
list1=[1,2,3,4,5] 
Largest = multiplication(list1) 
print(multiplication(list1)) 
