#  Faca um programa que leia 10 inteiros e imprima sua media.

soma = 0
for i in range(10):
    valor = int(input("Informe o valor"))
    soma += valor
print("A média é", soma/10)