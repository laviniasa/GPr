# Remova os espaços à esquerda da string:

txt = "     banana     "

x = txt.lstrip()

print("of all fruits", x, "is my favorite")

# O lstrip()método remove todos os caracteres iniciais 
# (o espaço é o caractere inicial padrão a ser removido


# Sintaxe
# string.lstrip(characters)

# Exemplo
# Remova os caracteres principais:
txt = ",,,,,ssaaww.....banana"

x = txt.lstrip(",.asw")

print(x)