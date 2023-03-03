# Faça um programa que leia três números e mostre-os em ordem decrescente


# criar uma lista vazia 'l' para receber os numeros

# para cada numero 'n' em um intervalo de 3

# vai pedir pra digitar um numero

# adicionar na lista 'l'

# fazer isso até acabar as 3 vezes

#  com a lista pronta ordenar a lista para ficar crescente *

# e depois reverter para ficar decrescente *

# por fim imprimir a lista 'l'

l = []

for n in range(3):
    e = int(input('Digite um numero: '))
    l.append(e)

l.sort()
l.reverse()
print(l)