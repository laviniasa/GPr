# Escreva um algoritmo que leia certa quantidade de n  ́umeros e imprima o maior deles e
# quantas vezes o maior n  ́umero foi lido. A quantidade de n  ́umeros a serem lidos deve ser
# fornecida pelo usu  ́ario

q = int(input('digite uma quantidade: '))
n = []
count = 0
for num in range(q):
    result = input('digite um numero: ')
    n.append(result)
for x in n:
    if x == max(n):
        count+=1
print(count)
print(max(n))