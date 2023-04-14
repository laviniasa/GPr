# Fac ̧ a um programa que leia um n  ́umero inteiro positivo  ́ımpar N e imprima 
# todos os numeros  ́ımpares de 1 at  ́e N em ordem crescente

impar = []

n = int(input("Digite o valor de n: "))

for i in range(1, n):
   if i % 2 != 0:
       impar.append(i)
print(i)
