# Faca um programa que some todos os n  ́umeros naturais abaixo de 1000 que s  ̃ao m  ́ultiplos
# de 3 ou 5.7


soma = 0

for i in range (1000):
   if i % 3 == 0:
       soma += i
   elif i % 5 == 0:
       soma += i
print(soma)