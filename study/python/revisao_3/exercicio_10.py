#Faça uma função que recebe um valor inteiro e verifica se o valor é par ou ímpar.
# A função deve retornar um valor booleano

def impar_par(n):
    resto = n % 2

    if resto == 0:
        return True
    else:
        return False

x = 1
print(impar_par(x))

