# O método format() serve para criar uma string que contem campos entre chaves a serem substituídos pelos argumentos de format. Abaixo um exemplo executado no ambiente interativo:

# >>> str = 'O filme {0} merece {1} estrelas'
# >>> str.format('Exterminador do Futuro', 4)
# 'O filme Exterminador do Futuro merece 4 estrelas'
# >>>
# Repare os campos de substituição na string estão associadas aos parâmetros de format por numeração dentro das chaves começando em zero para o primeiro parâmetro, 1 para o segundo parâmetro e continuando assim sucessivamente. Nada impede que se use um parâmetro mais de uma vez e fora de sua ordem como no exemplo abaixo:

# >>> str = '{0} é um {1} companheiro, {1} companheiro é o {0}, ninguém pode negar'
# >>> str.format('Paulo', 'bom')
# 'Paulo é um bom companheiro, bom companheiro é o Paulo, ninguém pode negar'
# >>> str.format('João', 'ótimo')
# 'João é um ótimo companheiro, ótimo companheiro é o João, ninguém pode negar'
# >>>


# ambém podemo usar campos nomeados, sendo que estes devem vir depois dos parâmetros simples no
#  método format, como exemplo crie o e teste o programa idade.py conforme o código abaixo:

# #!/usr/bin/env python3

# texto = '{0} tem {idade} anos de idade'
# print('Progama para calcular a idade de uma pessoa')
# print()

# nome = input('Entre com o nome da pessoa: ')
# print()

# a1 = int(input("Entre com o ano de nascimento: "))
# print()

# a2 = int(input("Entre com ano atual: "))
# print()
# print(texto.format(nome, idade = a2 - a1 ))
# Dentro dos campos a serem substituídos podemo especificar formatações numéricas ou para strings 
# usando as seguintes regras:

