# Leia um vetor de 40 posições. Contar e escrever quantos valores pares ele possui.

lista = []

valoresPares = 0

for i in range(len(lista)):
    if lista[i] % 2 == 0:
        valoresPares += 1

print ("Quantidade de valores pares: ", valoresPares)

# lista = []

# i = 0
# num = 0
# while len(lista) < 40:
#     if num % 2 == 0:
#         lista.append(num)
#         i += 1
#     num += 1 

# print(i)
