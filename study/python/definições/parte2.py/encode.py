# Encode (str) e Decode (bytes) É possível converter uma string em bytes ou bytes em string 
# usando os métodos encode da string ou decode de bytes.

# Esses métodos recebem dois argumentos. O primeiro argumento especifica a codificação de
#  caracteres desejada (utf-8 ou qualquer outra disponível em Standard Encodings – use utf-8 
#  sempre que possível). O segundo informa como os erros devem ser tratados


# Encode (str)
# Suponha que eu queira converter uma string UTF-8 para bytes UTF-8.

# Eu posso fazer isso da seguinte maneira:

# 1
# >>> meu_nome = 'Otávio'
# 2
# >>> meu_nome_em_bytes = meu_nome.encode('utf-8')
# 3
# >>> meu_nome_em_bytes
# 4
# b'Ot\xc3\xa1vio'
# 5
# >>> 

# De acordo com o código anterior, tudo ocorreu perfeitamente. 
# Isso porque converti uma string sabendo que ela tinha caracteres UTF-8 para bytes em UTF-8. 
# Mantendo a mesma codificação de caractere, não terei problemas.
