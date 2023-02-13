# Faça um programa que leia três números e mostre-os em ordem decrescente

#definir uma função 'decrescente' com um número inteiro 'n' como parâmetro

# criar uma lista 'l' vazia 

# definir um laço de loop for onde range vai percorrer o for 3 vezes

# acrecentar os numeros na lista 'l' com o método .append com o numero intero 'n' 
# como parâmetro

# então com o a função .sort() ordenar 'l' e como parâmetro ultililizar 
# a função reverse = True para deixar em ordem decrescente 

#por ultimo retornar 

def decrescente(n):
    l = []
    for i in range(3):
        l.append(n) 
        l.sort(reverse = True)
    return l


