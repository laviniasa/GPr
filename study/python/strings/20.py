# Escreva um programa que leia a idade e o primeiro nome de varias pessoas. Seu pro-
# grama deve terminar quando uma idade negativa for digitada. Ao terminar, seu programa
# deve escrever o nome e a idade das pessoas mais jovens e mais velhas.

v = []
j = []
a = 0
while a == 0:
    nome = str(input('digite seu nome'))
    idade = int(input('digite sua idade'))
    if idade < 0:
        print (v)
        print (j)
        break
    elif idade >= 50:
        v.append(nome)
        print('idoso')
    elif idade <= 25:
        j.append(nome)
        print('jovem')

