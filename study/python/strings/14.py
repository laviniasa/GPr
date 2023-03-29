# Ler uma frase e contar quantos caracteres sao brancos. Lembre-se que uma frase  ́e um
# conjunto de caracteres (vetor).7

def swapPositions(list, pos1, pos2): 
      
    list[pos1], list[pos2] = list[pos2], list[pos1] 
    return list
List = [23, 65, 19, 90] 
pos1, pos2  = 1, 3
  
print(swapPositions(List, pos1-1, pos2-1)) 