# Uma função que retorne uma matriz, onde cada sequência é uma lista seja uma linha,
#na ordem em que for recebida, adicionada de uma coluna que seja a soma das células de cada linha,
#e uma linha que seja a soma das células de cada coluna.


def matriz (seq1, seq2, seq3, seq4):

   matriz= []  
   
   soma = 0
   for linha in seq1:
      soma = (soma + linha)
   seq1.append(soma)
   matriz.append(seq1)

   soma = 0
   for linha in seq2:
      soma = (soma + linha)
   seq2.append(soma)
   matriz.append (seq2)
   
   soma=0
   for linha in seq3:
      soma = (soma + linha)
   seq3.append(soma)
   matriz.append (seq3)
   
   soma=0
   for linha in seq4:
      soma = (soma + linha)
   seq4.append(soma)
   
   matriz.append(seq4)

   arreySomaColl = []
   somaColl = 0
   i = 0 
   j = 0
   for linha in matriz:
      for coluna in linha:
            somaColl = somaColl + matriz[i][j]
            i= i + 1
      i = 0
      arreySomaColl.append(somaColl)
      somaColl = 0
      j = j + 1

   matriz.append(arreySomaColl)

   return matriz

arrey = [1,2,3]
arrey2 = [6,7,8]
arrey3 = [5,0,4]
arrey4 = [9,0,1]    

# matriz2 = []
# matriz2.extend([])
# matriz2.extend([])
# matriz2.extend([])
# matriz2.extend([])

test = matriz (arrey, arrey2, arrey3, arrey4)
for linha in test:
   print ("")
   for lugar in linha:
      print(  lugar, end=" ")
   print("")