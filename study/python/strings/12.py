# 12. Faca um programa que receba do usuario uma string. O programa imprime a string sem
# suas vogais.

a = 'lavinia'
b = 'aeiou'
for letra in range(0, len(b)):
    a = a.replace(b[letra], "")
print(a)
