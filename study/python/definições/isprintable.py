# Em Python, isprintable() é um método embutido usado para manipulação de strings.
# O método isprintable() retorna “True” se todos os caracteres na string são imprimíveis ou 
# a string está vazia, caso contrário, retorna “False”.
# Esta função é usada para verificar se o argumento contém algum caractere imprimível, como:

# Dígitos (0123456789)
# Letras maiúsculas (ABCDEFGHIJKLMNOPQRSTUVWXYZ)
# Letras minúsculas (abcdefghijklmnopqrstuvwxyz)
# Caracteres de pontuação (! ”# $% & '() * +, -./:;?@[\]^_` {|} ~)
# Espaço()

string = 'My name is Ayush'
print(string.isprintable()) 
string = 'My name is \n Ayush'
print(string.isprintable()) 
string = '' 
print( string.isprintable()) 


# Resultado:

# Verdade
# Falso
# Verdade