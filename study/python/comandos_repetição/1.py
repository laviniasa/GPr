# Faca um programa que determine e mostre os cinco primeiros multiplos de 3, conside-
# rando numeros maiores que 0

# n = 12
# num = []
# for i in range (0, n+1):
#     if (i % 3 == 0):
#         num.append(i)
# print (num)

m = 3
q = 5

soma = 0
lis = list()
while len(lis) < q:
    soma += m
    lis.append(soma)

print(lis)
    