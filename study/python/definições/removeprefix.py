# sintaxe
# str.removeprefix (prefixo, /)


# O método cria uma nova string a partir da string original removendo o prefixo passado como um 
# argumento. Formalmente, retorna string[len(prefix):]se a string começa com prefixe
# string[:]caso contrário. Assim, em qualquer caso, o resultado é uma nova string ou uma cópia
# da string original.

s = 'Hello World from Python 3.9!'
print(s.removeprefix('Hello World')) # from Python 3.9!
print(s.removeprefix('')) # Hello World from Python 3.9!

print(s.removesuffix('3.9!')) # Hello World from Python
print(s.removesuffix('Python')) # Hello World from Python 3.9! 