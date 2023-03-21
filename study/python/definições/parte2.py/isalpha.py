# Em Python, isalpha() é um método embutido usado para manipulação de strings.
# O método isalpha() retorna “True” se todos os caracteres na string forem alfabetos, caso
# contrário, retorna “False”.
# Esta função é usada para verificar se o argumento inclui apenas caracteres do alfabeto 

str.isalpha()

string = 'Ayush'
print(string.isalpha())
   
string = 'Ayush0212'
print(string.isalpha())
   
string = 'Ayush Saxena'
print( string.isalpha())

# Saída: 

# True
# False
# False

# O espaço não é considerado o alfabeto, portanto, retorna "Falso"