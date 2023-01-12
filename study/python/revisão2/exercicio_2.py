#Crie uma função que receba uma string s e um inteiro n como argumentos
# e retorne uma string com o valor s repetido n vezes.

def repeater(s, n):
    a = n * s
    return a

a = 'lavinia'
b = 5
test = repeater(a , b)
print(test)

def devide(a , b):
    d = a / b
    return d

test = devide(10, 2)
print(test)