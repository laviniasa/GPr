# Fac ̧ a um programa que receba dois n  ́umeros. 
# Calcule e mostre:
# •a soma dos numeros pares desse intervalo de n  ́umeros, incluindo os n  ́umeros digi-
# tados;
# •a multiplicac ̧  ̃ao dos n  ́umeros  ́ımpares desse intervalo, incluindo os digitados


n1 = input('digite um valor: ')
n2 = input('digite outro valor: ')

p = []

for num in range(n1, n2):
    if num % 2 == 0:
        p.append(num)
print (p)
        