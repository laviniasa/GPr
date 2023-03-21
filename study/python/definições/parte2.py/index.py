# Para retornar o índice do item que estamos querendo saber, precisamos passar para o método index(),
#  no mínimo, o parâmetro com o valor do item que estamos procurando.
#  Esse, no entanto, não é o único parâmetro que podemos usar no método index().

# lista.index(item, inicio, fim)

# item é o valor do item cujo índice estamos querendo pesquisar.
# inicio é um parâmetro opcional que indica o ponto de partida na lista onde a pesquisa deve começar. 
# Isso é bem útil quando temos um item repetido.
# fim indica o índice onde a pesquisa deve parar. Este parâmetro também é opcional.

listaDeNomes = ['Fulano', 'Fulana', 'DeTal', 'Ihechikara']

print(listaDeNomes.index('Fulana'))
# 1

# No código acima, criamos uma lista de nomes: listaDeNomes = ['Fulano', 'Fulana', 'DeTal', 'Ihechikara'].

# E usando o método index(), obtivemos o índice de "Fulana" na lista: listaDeNomes.index('Fulana').

# Foi impresso no console o resultado da busca, que retornou o valor 1.

# listas são indexadas a partir de zero – então, o primeiro item tem o índice 0, o segundo tem o índice 1 e assim por diante. Fica assim:

# 'Fulano' => índice 0
# 'Fulana' => índice 1
# 'DeTal' => índice 2
# 'Ihechikara' => índice 3