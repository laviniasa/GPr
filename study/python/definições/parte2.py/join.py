# O método join() é um método de string e retorna uma string na qual os
#  elementos da sequência foram unidos por um separador str.

# Sintaxe:

# string_name .join (iteráveis)
# string_name : É o nome da string em que
#              elementos unidos de iterável serão
#              armazenado.

# Parâmetros: O método join() é iterável - objetos capazes de retornar seus membros um de cada vez. Alguns exemplos são Lista, Tupla, String, Dicionário e Conjunto

# Valor de retorno: O método join() retorna uma string concatenada com os elementos de iterable .

# Erro de tipo : se o iterável contiver qualquer valor que não seja de string, ele gerará uma exceção TypeError.

list1 = ['1','2','3','4']  
  
s = "-"
s = s.join(list1) 
print(s) 

# Resultado:

1-2-3-4