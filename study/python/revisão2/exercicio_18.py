# Faça um programa que peça um número inteiro e determine se ele é ou não um número primo.
#  Um número primo é aquele que é divisível somente por ele mesmo e por 1.

def primos(n):
    mult=0

    for count in range(2,n):
        if (n % count == 0):
            #print("Múltiplo de",count)
            mult += 1

    if(mult==0):
        print("É primo")
    else:
        print("não é primo")

n = int(input("Verificar numeros primos : "))
test = primos(n)
print(test)