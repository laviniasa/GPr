#- Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas.
#Imprima as consoantes.

n_char = int(input("Informe o numero caracteres: "))
lista_char = []

for i in range (0,n_char):
    caracteres = str(input(f"Insira o {i+1} caractere: "))
    lista_char.append(caracteres)
print("Lista de caracteres: ",lista_char)

def conta_consoante(lista_char):
    soma = 0
    for i in lista_char:
        if i == 'a' or i == 'e' or i == 'i' or i == 'o'or i == 'u':
            soma = 0
        else:
            soma += 1
    print("Soma de consoantes: ",soma)
    return soma

conta_consoante(lista_char)

