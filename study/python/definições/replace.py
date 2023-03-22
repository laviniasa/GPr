# O método Python replace é usado para substituir trechos de uma string por uma ou mais vezes.
#  Também podemos utilizar o módulo re, no qual podemos aplicar expressões regulares para refinar
#  ainda mais as condições de substituição. Portanto, a linguagem oferece diversos recursos para a
#  manipulação de strings.


# O método replace() contém dois parâmetros obrigatórios e um opcional. Sua sintaxe é:

# string.replace(oldvalue, newvalue, count)


linguagens="Python\nJavaScript\nC\nRuby"
print(linguagens.replace("\n", ", "))

#Resultado: Python, JavaScript, C, Ruby