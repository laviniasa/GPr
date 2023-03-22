# Substitua quaisquer caracteres "S" por um caractere "P":

#use a dictionary with ascii codes to replace 83 (S) with 80 (P):
mydict = {83:  80}
txt = "Hello Sam!"
print(txt.translate(mydict))

# resposta

# Hello Pam!

# Definição e Uso
# O translate()método retorna uma string onde alguns caracteres especificados são substituídos pelo caractere descrito em um dicionário ou em uma tabela de mapeamento.

# Use o maketrans()método para criar uma tabela de mapeamento.

# Se um caractere não for especificado no dicionário/tabela, o caractere não será substituído.

# Se você usar um dicionário, deverá usar códigos ascii em vez de caracteres.

# Sintaxe
# string.translate(table)

# Exemplo
# Use uma tabela de mapeamento para substituir "S" por "P":

txt = "Hello Sam!"
mytable = str.maketrans("S", "P")
print(txt.translate(mytable))