#1.4 - Uma função deve retornar a divisão do maior número pelo menor número

def division(list1): 
    l = len(list1)
    return max(list1)/min(list1)
    
list1=[2,3,4,5,10] 
Largest = division(list1) 
print(division(list1)) 
