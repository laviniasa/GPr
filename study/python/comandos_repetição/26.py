# Faca um algoritmo que encontre o primeiro multiplo de 11, 13 ou 17 ap  ́os um n  ́umero
# dado.

n = 1
multiplos = []
for i in range(1, n + 1):
    multiplos.append(11 * i)
print(multiplos)