# Remova todos os espaços em branco no final da string:

txt = "     banana     "

x = txt.rstrip()

print("of all fruits", x, "is my favorite")

# resposta
# of all fruits     banana is my favorite

# O rstrip()método remove todos os caracteres finais (caracteres no final de uma string),
#  o espaço é o caractere final padrão a ser removido.

# Sintaxe
# string.rstrip(characters)

# Exemplo
# Remova os caracteres finais se forem vírgulas, pontos, s, q ou w:

txt = "banana,,,,,ssqqqww....."

x = txt.rstrip(",.qsw")

print(x)