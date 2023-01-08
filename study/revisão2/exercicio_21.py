#uma fucao deve retornar para cada numero a informação: "Impar" ou "Par"


def test(n):
    if (n%2) == 0:
        print("Par")
    else:
        print("Ímpar")

numero = int(input('Digite um inteiro: '))

teste = test(numero)
print(teste)