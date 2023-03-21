# Em Python, isspace() é um método embutido usado para manipulação de strings.
#  O método isspace() retorna “True” se todos os caracteres da string forem espaços em branco,
#  caso contrário, retorna “False”.
# Esta função é usada para verificar se o argumento contém todos os caracteres de espaço em 
# branco, como:

# '' - Espaço
# '\ t' - Aba horizontal
# '\ n' - Nova linha
# '\ v' - Guia vertical
# '\ f' - Feed
# '\ r' - Retorno de carro


string = 'Geeksforgeeks'
  
print(string.isspace()) 
   
string = '\n \n \n'
  
print(string.isspace()) 
  
string = 'Geeks\nfor\ngeeks'
print( string.isspace()) 

# Resultado:

# Falso
# Verdade
# Falso