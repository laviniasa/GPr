# Coloque a primeira letra de cada palavra em maiúscula:

txt = "Welcome to my world"

x = txt.title()

print(x)

# resposta
# Welcome To My World

# Definição e Uso
# O title()método retorna uma string em que o primeiro caractere de cada palavra é maiúsculo. Como um cabeçalho ou um título.

# Se a palavra contiver um número ou um símbolo, a primeira letra depois disso será convertida em maiúscula.

# Sintaxe
# string.title()


# Exemplo
# Coloque a primeira letra de cada palavra em maiúscula:

txt = "Welcome to my 2nd world"

x = txt.title()

print(x)

# Exemplo
# Observe que a primeira letra após uma letra não alfabética é convertida em uma letra maiúscula:

txt = "hello b2b2b2 and 3g3g3g"

x = txt.title()

print(x)
