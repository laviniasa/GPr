# Faca um programa que, dada uma string, diga se ela  ́e um palindromo ou nao. Lem-
# brando que um palındromo  ́e uma palavra que tenha a propriedade de poder ser lida
# tanto da direita para a esquerda como da esquerda para a direita. Exemplo:
# ovo
# arara
# Socorram-me, subi no onibus em Marrocos.
# Anotaram a data da maratona


def result(palavra):
    palavra_min = palavra.lower()
    palavra_invertida = palavra_min[::-1]
    if palavra_min == palavra_invertida:
        print("A palavra é palíndroma.")
    else:
        print("A palavra não é palíndroma.")
    print()
    print('Sua palavra: ', end='')
    print(palavra)
    print('Inversão: ', end='')
    print(palavra_invertida)


word=input('Digite uma palavra: ')
print(result(word))