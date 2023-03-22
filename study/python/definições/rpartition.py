# Pesquise a última ocorrência da palavra "bananas" e retorne uma tupla com três elementos:

# 1 - tudo antes do "jogo"
# 2 - o "jogo"
# 3 - tudo depois do "jogo"

txt = "I could eat bananas all day, bananas are my favorite fruit"

x = txt.rpartition("bananas")

print(x)

# resposta
# ('I could eat bananas all day, ', 'bananas', ' are my favorite fruit')

# O rpartition()método procura a última ocorrência de uma string especificada e divide a string em uma tupla contendo três elementos.

# O primeiro elemento contém a parte antes da string especificada.

# O segundo elemento contém a string especificada.

# O terceiro elemento contém a parte após a string.

# Sintaxe
# string.rpartition(value)


# Se o valor especificado não for encontrado, o método rpartition() retorna uma tupla contendo: 1 - 
# uma string vazia, 2 - uma string vazia, 3 - a string inteira:

txt = "I could eat bananas all day, bananas are my favorite fruit"

x = txt.rpartition("apples")

print(x)


