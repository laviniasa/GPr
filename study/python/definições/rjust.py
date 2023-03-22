# Retorne uma versão de 20 caracteres justificada à direita da palavra "banana":

txt = "banana"

x = txt.rjust(20)

print(x, "is my favorite fruit.")

# resposta
#               banana é minha fruta favorita.

# Nota: No resultado, existem 14 espaços em branco à esquerda da palavra banana.

# O rjust()método alinhará a string à direita, usando um caractere especificado 
# (espaço é o padrão) como caractere de preenchimento.

# Sintaxe
# string.rjust(length, character)

# Exemplo
# Usando a letra "O" como caractere de preenchimento:

txt = "banana"

x = txt.rjust(20, "O")

print(x)

# resposta
# OOOOOOOOOOOOO banana