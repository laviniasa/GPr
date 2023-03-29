# 10. Entre com um nome e imprima o nome somente se a primeira letra do nome for “a”
# (maiuscula ou minuscula)


def program(s):
    if s.lower()[0] == 'a':
        return s
    else:
        return 'por favor outro nome'
    
x = 'Ana'
print(program(x))