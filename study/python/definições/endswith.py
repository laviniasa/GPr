# a função endswith retorna 1 se a substring estiver contida no final da string.

# A função startswith() é usada para verificar se uma determinada frase começa com alguma 
# string particular.
# Os parâmetros de início e término são opcionais.
# Podemos usá-los quando quisermos que apenas alguma substring particular da string original 
# seja considerada para pesquisa.
 
# Retorna:
# o valor de retorno é binário. A função retorna True se a frase original começar com search_string,
#  senão False .

# Sintaxe:

# str.endswith (search_string, start, end)

txt = "Hello, welcome to my world."

x = txt.endswith(".")

print(x)