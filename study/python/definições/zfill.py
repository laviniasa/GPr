# Preencha a string com zeros até que ela tenha 10 caracteres:

txt = "50"

x = txt.zfill(10)

print(x)

# resposta
# 0000000050

# Definição e Uso
# O zfill()método adiciona zeros (0) no início da string, até atingir o comprimento especificado.

# Se o valor do parâmetro len for menor que o comprimento da string, nenhum preenchimento é feito.

# Sintaxe
# string.zfill(len)