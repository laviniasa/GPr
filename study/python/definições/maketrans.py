# Exemplo
# Crie uma tabela de mapeamento e use-a no translate()método para substituir quaisquer
#  caracteres "S" por um caractere "P":

txt = "Hello Sam!"
mytable = str.maketrans("S", "P")
print(txt.translate(mytable))

# O maketrans()método retorna uma tabela de mapeamento que pode ser usada com o método
#  para substituir os caracteres especificados. translate()


# sintaxe
# str.maketrans(x, y, z)

# Exemplo

txt = "Hi Sam!"
x = "mSa"
y = "eJo"
mytable = str.maketrans(x, y)
print(txt.translate(mytable))

# Exemplo
# O terceiro parâmetro descreve os caracteres que você deseja remover da string:

txt = "Good night Sam!"
x = "mSa"
y = "eJo"
z = "odnght"
mytable = str.maketrans(x, y, z)
print(txt.translate(mytable))

# Exemplo
# O maketrans()próprio método retorna um dicionário descrevendo cada substituição, em unicode:

txt = "Good night Sam!"
x = "mSa"
y = "eJo"
z = "odnght"
print(str.maketrans(x, y, z))