#- Faça uma função que recebe um valor inteiro e verifica se o valor é positivo ou negativo.
#  A função deve retornar um valor booleano.

def funcao(n):
    if n > 0:
        return True
    elif n == 0:
        return True
    else:
        return False

v = -1

test = funcao(v)
print(test)