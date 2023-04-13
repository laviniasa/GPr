# Escreva um programa que leia um n  ́umero inteiro 
# e calcule a soma de todos os divisores
# desse n  ́umero, com excec ̧  ̃ao dele pr  ́oprio. Ex: a soma dos divisores do n  ́umero 66  ́e
# 1 + 2 + 3 + 6 + 11 + 22 + 33 = 78

divisor = 1
d = []
count = 0
numero = int(input('Informe um número inteiro e positivo: '))
if numero < 0:
    numero = int(input(' Digite um número inteiro e positivo: '))
for divisor in range(divisor, numero):
    if numero % divisor == 0:
        d.append(divisor)
        print(divisor)
for num in d:
    count = count + 2