#Crie uma função que dado um número inteiro n retorna o 
# somatorio dos números de 0 a n


def sum (n):
    soma = 0
    for n in range(0, n + 1):
        soma = soma + n
    return soma

a = 2

test = sum(a)
print(test)