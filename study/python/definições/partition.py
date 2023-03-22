# Pesquise a palavra "bananas" e retorne uma tupla com três elementos:

# 1 - tudo antes do "jogo"
# 2 - o "jogo"
# 3 - tudo depois do "jogo"

txt = "I could eat bananas all day"

x = txt.partition("bananas")

print(x)

# O partition()método procura uma string especificada e divide a string em uma tupla contendo três
#  elementos.

# O primeiro elemento contém a parte antes da string especificada.

# O segundo elemento contém a string especificada.

# O terceiro elemento contém a parte após a string.

# Sintaxe
# string.partition(value)

# Exemplo
# Se o valor especificado não for encontrado, o método partition() retorna uma tupla contendo: 1 - a string inteira, 2 - uma string vazia, 3 - uma string vazia:

txt = "I could eat bananas all day"

x = txt.partition("apples")

print(x)
