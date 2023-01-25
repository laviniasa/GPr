#Leia um vetor de 20 posições e em seguida um valor X qualquer.
#Seu programa devera fazer uma busca do valor de X no vetor lido
#e informar a posição em que foi encontrado ou se não foi encontrado.

lista = [16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1,0,20,19,18]

a = False
valor = int(input("valor para buscar"))

for i in range(len(lista)):
    if lista[i] == valor:
        print("Valor encontrado na posição: ", i)
        a = True
        break

if(not a):
    print("valor não encontrado")

