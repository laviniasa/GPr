# Crie uma função que receba um parâmetro n e retorna uma 
# lista de n números inteiros aleatórios.

import random
def list_random(n):
    lista = []

    for i in range(n):
        lista.append(random.randint(0, 100))
    return lista

test = list_random(5)
print(test)