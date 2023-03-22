# Remova os espaços no início e no final da string:

txt = "     banana     "

x = txt.strip()

print("of all fruits", x, "is my favorite")

# resultado

# of all fruits banana is my favorite


# Definição e Uso
# O strip()método remove todos os caracteres iniciais (espaços no início) e finais (espaços no final) (espaço é o caractere inicial padrão a ser removido)

# Sintaxe
# string.strip(characters)


# Exemplo
# Remova os caracteres iniciais e finais:

txt = ",,,,,rrttgg.....banana....rrr"

x = txt.strip(",.grt")

print(x)