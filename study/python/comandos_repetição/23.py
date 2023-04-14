# Faca um algoritmo que leia um n  ́umero positivo e imprima seus divisores

divisor = 1

numero = int(input('Informe um número inteiro e positivo: '))
if numero < 0:
    numero = int(input(' Digite um número inteiro e positivo: '))
for divisor in range(divisor, numero):
    if numero % divisor == 0:
        print(divisor)