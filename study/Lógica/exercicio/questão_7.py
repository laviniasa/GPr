# Leia uma matriz 6 x 6, conte e escreva quantos valores maiores que 10 ela possui.


# definir uma função matriz onde tem seq1, seq2, seq3, seq4, seq5, seq6 como parametro

# criar uma variavel 'vazia'

# criar variavel soma igual a 0

# ultilizar o laço de loop for 'linha' na primeira sequencia 

# com a condição if - se linha >10 

# atualizar soma onde vai ser soma + 1

# adicionar ao final da lista 

# o mesmo acontece com as demais sequencias 

# retornar matriz   


def matriz(seq1, seq2, seq3, seq4):

   matriz = []  
   
   soma = 0
   for linha in seq1:
      linha > 10 
      soma = soma +1

   matriz.append(soma)

   soma = 0
   for linha in seq2:
      soma = (soma + linha )
      

   seq2.append(soma)
   matriz.append(seq2)
   
   soma=0
   for linha in seq3:
      soma = (soma + linha)

   seq3.append(soma)
   matriz.append(seq3)
   
   soma = 0
   for linha in seq4:
      soma = (soma + linha)

   seq4.append(soma)
   matriz.append(seq4)

   return matriz
arrey = [1,2,3]
arrey2 = [6,7,8]
arrey3 = [5,0,4]
arrey4 = [9,0,1]    

matriz2 = []
matriz2.extend([1])
matriz2.extend([6])
matriz2.extend([5])
matriz2.extend([9])

test = matriz (arrey, arrey2, arrey3, arrey4)
#matriz2.append(test) 
for linha in test:
   print("")
   for lugar in linha:
      print(  lugar, end=" ")
   print(" ")


