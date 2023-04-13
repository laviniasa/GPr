# Faca um programa que peca ao usuario para digitar 10 valores e some-os.


valores = []
soma = 0
for num in range(3):
    a = int(input('digite um valor'))
    valores.append(a)
    x = sum(valores)
print(x)