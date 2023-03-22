# Divida uma string em uma lista onde cada linha é um item de lista:

txt = "Thank you for the music\nWelcome to the jungle"

x = txt.splitlines()

print(x)

# resultado
# ['Thank you for the music', 'Welcome to the jungle']


# Definição e Uso
# O splitlines()método divide uma string em uma lista. A divisão é feita nas quebras de linha.

# Sintaxe
# string.splitlines(keeplinebreaks)


# Exemplo
# Divida a string, mas mantenha as quebras de linha:

txt = "Thank you for the music\nWelcome to the jungle"

x = txt.splitlines(True)

print(x)