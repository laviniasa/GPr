#1.5 - Uma função deve retornar, para cada número a informação: “Impar”, ou “Par”

def impar_par(n):
    list1 = [n]
    for c in list1:
        if c % 2 == 0:
            return "Par"
        else:
            return "Impar"

x = [1,2,3,4,5,6,7,8,9,10]
teste = impar_par(x)
print(teste(x))