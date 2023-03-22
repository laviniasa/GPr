# O método Python split é uma das funções disponíveis em Python utilizada para a manipulação 
# de strings. Na prática, ele permite dividir o conteúdo da variável de acordo com as condições 
# especificadas em cada parâmetro da função ou com os valores predefinidos por padrão.


# sintaxe
# string.split(separator, maxsplit)

# string: corresponde ao nome da variável que servirá de base para a divisão;
# separator: indica o caractere utilizado como separador da string;
# maxsplit: representa a quantidade máxima de divisões realizadas.

# Como mencionamos, o método split() pode ser executado sem nenhum parâmetro. Nesse caso,
#  o caractere separador será o espaço (valor padrão) e a quantidade máxima de divisão será até
#  que o último caractere seja lido. Veja um exemplo:

nome = "João Paulo da Silva"
print(nome.split())
#resultado ['João', 'Paulo', 'da', 'Silva']


# Como mencionamos, o método split() contém dois parâmetros para determinar como será realizada 
# a separação do conjunto de caracteres da string. Confira cada um deles a seguir.

# Separator
# O separator corresponde ao caractere que será utilizado como identificador do ponto de 
# separação do conteúdo da string. Esse parâmetro não é obrigatório. Portanto, se nada for
#  informado, o compilador entenderá que a divisão será feita sempre que for encontrado um
#  caractere de espaço.

# Podemos utilizar outro caractere para a divisão, como a vírgula, a barra, etc., que deve
#  ser escrito entre aspas simples ou dupla. Veja um pequeno exemplo:

# nomes = "João Paulo/Maria Paula/Ana Beatriz/José Pedro"
# print(nomes.split('/'))
# #resultado: ['João Paulo', 'Maria Paula', 'Ana Beatriz', 'José Pedro']
# Perceba que, apesar de haver o caractere de espaço na string (na separação dos nomes compostos),
#  ele não foi utilizado como separador, pois indicamos a barra para essa finalidade. Por isso,
#  o resultado apresentado foi uma lista com os quatro nomes contidos na variável.

# Vale ressaltar que o caractere utilizado como separador será eliminado da lista de retorno. 
# Portanto, perceba que não há a exibição da barra em nenhum elemento da lista. 


# Maxsplit
# O parâmetro maxsplit indica a quantidade de vezes em que a string será dividida. 
# O valor padrão é “-1”. Isso significa que a divisão será feita enquanto houver o caractere 
# separador e até que toda a string seja percorrida.

# Apesar de o parâmetro separator ser opcional, ele será obrigatório se quisermos utilizar 
# o parâmetro maxsplit. Entretanto, podemos declará-lo como “None”, pois ele representará o 
# valor padrão, ou seja, o caractere de espaço. Isso porque o método split() contém dois parâmetros 
# e se informarmos apenas um, ele retornará um erro de execução. Veja um exemplo:

nome = "João Paulo Menezes da Silva"
print(nome.split(None, 2))
#resultado: ['João', 'Paulo', 'Menezes da Silva']

print(nome.split(" ", 2))
#resultado: ['João', 'Paulo', 'Menezes da Silva']

print(nome.split(2))
'''
resultado: 
    print(nome.split(2))
TypeError: must be str or None, not int
'''
# Outra observação importe sobre o parâmetro maxsplit, é que após ele dividir a string original 
# pela quantidade de vezes determinada, todo o restante da string fará parte do resultado como
#  um único elemento da lista. Por isso, no nosso exemplo temos “João” e “Paulo” separados e 
# “Menezes da Silva” em um único elemento.

