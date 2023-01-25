#Leia um vetor de 12 posições e em seguida ler também dois valores X e Y quaisquer
#correspondentes a duas posições no vetor. 
# Ao final seu programa deverá escrever a soma dos valores encontrados 
# nas respectivas posições X e Y.                                                                                                                                                                                                                                                                                                                         

lista = [12,5,4,7,8,6,41,23,5,6,12]
x = int(input("primeira posição"))
y = int(input("segunda posição"))

resultado = lista[x] + lista[y]

print(resultado)