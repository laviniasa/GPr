# Divida uma string em uma lista, usando vírgula, seguida por um espaço (, ) como separador:

txt = "apple, banana, cherry"

x = txt.rsplit(", ")

print(x)

# resposta
# ['apple', 'banana', 'cherry']

# O rsplit()método divide uma string em uma lista, começando pela direita.

# Se nenhum "max" for especificado, este método retornará o mesmo que o split()método.


# Sintaxe
# string.rsplit(separator, maxsplit)

# Observação: quando maxsplit for especificado, 
# a lista conterá o número especificado de elementos mais um .


# Exemplo
# Divida a string em uma lista com no máximo 2 itens:

txt = "apple, banana, cherry"

x = txt.rsplit(", ", 1)

print(x)