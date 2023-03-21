# FUNÇÃO count()
# A função count() retorna a quantidade de vezes que um mesmo elemento está contido numa lista. 
# Essa é uma excelente maneira que evita a implementação de um 
# Laço de Repetição em busca de elementos iguais.

# No código a seguir, defimos uma lista e em seguida, invocamos a função count(), 
# pergunta assim, quantas vezes um determinado número existe nessa lista.

# #coding: utf-8

# >>> [1,2,3,4,5].count(1)
# 1
# >>> [1,2,3,4,5].count(4)
# 1
# >>> [1,2,3,4,5,4].count(4)
# 2
# Observamos, que quando o número 4 não estava repetido, a função count(4) retornou 1. 
# A partir do momento em que adicionamos mais uma vez o número 4, o valor retornado foi 2.

# A função count() também pode ser utilizada para saber se um determinado elemento está contido,
#  até porque, se o valor retornado for igual a 0, sabemos, que determinado elemento ainda não foi 
# adicionado.