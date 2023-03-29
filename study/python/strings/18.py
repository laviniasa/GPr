# Leia um vetor contendo letras de uma frase inclusive os espacos em branco. Retirar os
# espacos em branco do vetor e depois escrever o vetor resultante

cadeia = 'LAVINIA BARBOSA DE SA'
l = []
for letra in cadeia:
    if letra != ' ':
        l.append(letra)
print(l)