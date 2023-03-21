# O islower()método retorna True se todos os caracteres estiverem em minúsculas, caso contrário, False.

# Números, símbolos e espaços não são verificados, apenas caracteres do alfabeto.

# Sintaxe
# string.islower()


txt = "hello world!"

x = txt.islower()

print(x)

a = "Hello world!"
b = "hello 123"
c = "mynameisPeter"

print(a.islower())
print(b.islower())
print(c.islower())


# saida

# Falso
# Verdadeiro
# Falso