# O isprintable() retornará True quando todos os caracteres são visíveis quando manda imprimi-los, 
# isto incluindo os óbvios, mas também alguns menos óbvios como os que geram espaço em branco que não
#  deixam de serem imprimíveis. Um exemplo de caractere não imprimível é o nulo (\0). Ele tem que 
# ocupar espaço em tela ou papel.

# O mais comum de usá-lo é saber que se ele contará para determinar o espaço ocupado em uma 
# impressão qualquer em qualquer suporte ou se poderá causar algum erro por que criar uma situação
#  inesperada, por exemplo um \8 que é um backspace, então ele pode retroceder um caractere, então 
# em vez de ocupar mais um caractere ele ocupa 
# menos, apagando o anterior.


string = "Geeks for Geeks"
print(string.isidentifier())
  
string = "GeeksforGeeks"
print(string.isidentifier())
  
string = ""
print(string.isidentifier())
  
string = "Geeks0for0Geeks"
print(string.isidentifier())
  
string = "54Geeks0for0Geeks"
print(string.isidentifier())

# Saída: 

False
True
False
True
False