# Escreva um programa que declare um inteiro, inicialize-o com 0, e incremente-o de 1000
# em 1000, imprimindo seu valor na tela, ate que seu valor seja 100.000 (cem mil)

x = 0
while True:
   x = x + 1000
   print(x)
   if(x == 100000):
       break