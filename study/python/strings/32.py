# Faca um programa que contenha um menu com as seguintes opcoes:

a = 0 
while a == 0:
    resp = input(str(input('escolha uma opção:(1-a/2-b/): ')).lower())
    if resp == 1:
        s1 = input('digite um nome')
        if len(s1) > 20:
            print('tamanho maximo 20 caracteres')
        else:
            print(s1)
    



# (a) Ler uma string S1 (tamanho maximo 20 caracteres);

# s1 = input('digite um nome')
# if len(s1) > 20:
#     print('tamanho maximo 20 caracteres')
# else:
#     print(s1)

# (b) Imprimir o tamanho da string S1;

# s1 = 'lavinia'
# # print(len(s1)) 

# (c) Comparar a string S1 com uma nova string S2 fornecida pelo usu  ́ario e imprimir o
# resultado da comparacao;

# s1 = 'lavinia'
# s2 = input('digite uma palavra')
# if s1 == s2:
#     print(True)
# else:
#     print (False) 


# (d) Concatenar a string S1 com uma nova string S2 e imprimir na tela o resultado da
# concatenacao;

# s1 = 'lavinia'
# s2 = input('digite uma palavra')
# result = s1 + s2
# print (result)    

# (e) Imprimir a string S1 de forma reversa;

# s1 = "lavinia"[::-1]
# print(s1)

# (f) Contar quantas vezes um dado caractere aparece na string S1. Esse caractere
# deve ser informado pelo usuario;

# s1 = 'lavinia'
# caracter = 'a'
# count = 0

# for c in s1:
#     if c == caracter:
#         count = count + 1
# print(count)

# (g) Substituir a primeira ocorrencia do caractere C1 da string S1 pelo caractere C2. Os
# caracteres C1 e C2 serao lidos pelo usuario;


# s = 'lavinia'
# c2 = 'w'
# x = s.replace(s[:1], c2)
# print(x)

# (h) Verificar se uma string S2  ́e substring de S1. A string S2 deve ser informada pelo
# usuario;

# s1 = 'string no Python'
# s2 = input('informe uma string')
# result = (s1.find(s2))
# if result == -1:
#     print('não é substring')
# else:
#     print('é substring de s2')


# (i) Retornar uma substring da string S1. Para isso o usuario deve informar a partir de
# qual posicao deve ser criada a substring e qual  ́e o tamanho da substrin

