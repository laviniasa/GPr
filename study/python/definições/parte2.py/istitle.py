# O método Python String istitle() retorna True se a string é uma string com título, caso contrário, 
# retorna False. O que é titulado? A string que tem o primeiro caractere em cada palavra maiúscula e 
# todos os caracteres restantes em letras minúsculas. 

# Sintaxe: 

# string.istitle()

# Retorna: 

# Verdadeiro se a string for uma string com título, caso contrário, retorna False.

s = 'Geeks For Geeks'
print(s.istitle())
  
s = 'geeks For Geeks'
print(s.istitle())
  
s = 'Geeks For GEEKs'
print(s.istitle())
  
s = '6041 Is My Number'
print(s.istitle())
  
s = 'GEEKS'
print(s.istitle())


# Saída: 

True
False
False
True
False