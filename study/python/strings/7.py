# 7. Ler nome, sexo e idade. Se sexo for feminino e idade menor que 25, imprime o nome da
# pessoa e a palavra “ACEITA”, caso contr  ́ario imprimir “NAO ACEITA

def program(nome, sexo, idade):
    n = nome
    s = sexo 
    i = idade
    if i < 25 and s == 'f':
        return nome + 'ACEITA'
    else:
        return 'NÃO ACEITA'

x = 'Lavinia'
y = 'f'
z = 18

print(program(x,y,z))
