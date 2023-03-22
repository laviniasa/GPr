# Se a string terminar com o sufixo e o sufixo não estiver vazio, a função str.removesuffix(suffix, /)
# remove o sufixo e retorna o restante da string. Se a string do sufixo não for encontrada, ela
#  retornará a string original. É introduzido na versão Python 3.9.0.

# Sintaxe: str.removesuffix(suffix, /)

print('ComputerScience'.removesuffix('Science'))
# suffix doesn't exist
print('GeeksforGeeks'.removesuffix('for'))

# saída                     
# Computer
# GeeksforGeeks



string1 = "Welcome to python 3.9"

print("Original String 1 : ", string1)


result = string1.removesuffix("3.9")

print("New string : ", result)

string2 = "Welcome Geek"

print("Original String 2 : ", string2)

# suffix doesn't exist

result = string2.removesuffix("Welcome")

print("New string : ", result)


# Original String 1 :  Welcome to python 3.9
# New string :  Welcome to python 
# Original String 2 :  Welcome Geek
# New string :  Welcome Geek
