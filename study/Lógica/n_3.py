# Faça uma função que recebe um valor inteiro e verifica se o valor é 
# positivo ou negativo.A função deve retornar um valor booleano.

# criar uma função positive_negative com um valor n inteiro como parametro

# se o numero for menor que zero

# retornar o valor booleano False

# se não retornar o valor booleano True

def positive_negative(n):
    if n < 0:
        return False
    else:
        return True

x = int(input('digite um valor'))

print (positive_negative(x))