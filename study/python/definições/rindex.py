# Onde no texto está a última ocorrência da string "casa"?:

txt = "Mi casa, su casa."

x = txt.rindex("casa")

print(x)

# resultado
# 12


# O rindex()método encontra a última ocorrência do valor especificado.

# O rindex()método gera uma exceção se o valor não for encontrado.

# O rindex()método é quase o mesmo que o rfind()método. Veja o exemplo abaixo.

# Sintaxe
# string.rindex(value, start, end)


# O método rindex() é semelhante ao método rfind() para strings. A única diferença é que rfind() 
# retorna -1 se a substring não for encontrada, enquanto rindex() lança uma exceção.
