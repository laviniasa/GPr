# Faca um programa que leia um numero inteiro positivo impar N e imprima todos os
# numeros ́ımpares de 1 ate N em ordem decrescente


v = []
n = int(input("Digite o valor de n: "))
if n -1 < 0:
    print('numero inválido')
    n = int(input("Digite outro valor: "))
elif n % 2 == 0:
    print('numero invalido')
    n = int(input("Digite outro valor: "))
count = 0
for num in range(1, n):
    if num % 2 != 0:
        v.append(num)
        v.sort()
        v.reverse()
print(v)
    