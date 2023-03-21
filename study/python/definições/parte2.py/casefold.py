# casefold é similar a lower , porém é mais "agressivo"

# O algoritmo em si é bem complicado, com definições que se estendem por várias páginas,
#  mas o ponto é que os algoritmos de lowercasing e casefolding usam regras diferentes. 
# Claro que para muitos casos o resultado é o mesmo, mas existem diferenças importantes
#  que justificam a existência desses dois métodos distintos.

# Um caso clássico é o caractere ß (LATIN SMALL LETTER SHARP S), que não é modificado por 
# lower por já ser uma letra minúscula (ele faz parte da categoria "Letter, lowercase"), 
# mas é modificado por casefold (o resultado é ss):

# s = 'ß'
# print(s.islower()) # True
# print(s.lower()) # ß
# print(s.casefold()) # ss

# O fato de usar um algoritmo diferente (e mais complicado) faz com que casefold nem sempre 
# retorne caracteres minúsculos. Por exemplo, para o caractere Ꮛ (CHEROKEE LETTER QUV), que é uma 
# letra maiúscula, casefold retorna sua versão em maiúscula