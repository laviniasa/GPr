# Leia um vetor de 12 posições e em seguida ler também dois valores X e Y quaisquer 
# correspondentes a duas posições no vetor. Ao final seu programa deverá escrever a 
# soma dos valores encontrados nas respectivas posições X e Y.

# deifinir um vetor 'l' com 12 numeros 

# escolher a primeira posiçao e guardar em uma variavel x
# escolher a segunda posição e guardar em uma variavel y

# somar da lista 'l' o valor 'x' mais 'y' guardar valor em result

# por fim imprimir result


l = [12,5,4,7,8,6,41,23,5,6,12]

x = int(input("primeira posição"))
y = int(input("segunda posição"))

result = l[x] + l[y]

print(result)