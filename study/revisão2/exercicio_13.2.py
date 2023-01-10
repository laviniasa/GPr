# Ao receber 4 sequencias de números
# Uma função que retorne uma matriz, onde cada sequência é uma lista seja uma coluna,
# na ordem em que for recebida, adicionada de uma coluna
#  que seja a soma das células de cada linha, 
# e uma linha que seja a soma das células de cada coluna.

def matriz (seq1, seq2, seq3, seq4):

   matriz= []  
   
   soma = 0
   for linha in seq1:
      soma = (soma + linha)

   matriz.append(seq1)
   matriz.extend(soma)
   
   soma = 0
   for linha in seq2:
      soma = (soma + linha)

   matriz.append(seq2)
   matriz.extend (soma)
   
   soma=0
   for linha in seq3:
      soma = (soma + linha)

   matriz.append(seq3)
   matriz.extend(soma)
   
   soma=0
   for linha in seq4:
      soma = (soma + linha)

   matriz.append(seq4)
   matriz.extend (soma)

   return matriz
arrey = [1,2,3]
arrey2 = [6,7,8]
arrey3 = [5,0,4]
arrey4 = [9,0,1]    

matriz2 = []
matriz2.append(arrey)
matriz2.append(arrey2)
matriz2.append(arrey3)
matriz2.append(arrey4)

test = matriz (arrey, arrey2, arrey3, arrey4)
#matriz2.append(test) 
print(test)
for linha in test:
   for lugar in linha:
      print(lugar, end=" - ")
   print("")





