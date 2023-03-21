# O isdecimal()método retorna True se todos os caracteres forem decimais (0-9).

# Este método é usado em objetos unicode.


# Sintaxe
# string.isdecimal()


a = "\u0030" #unicode for 0
b = "\u0047" #unicode for G

print(a.isdecimal())
print(b.isdecimal())

# true
# flase