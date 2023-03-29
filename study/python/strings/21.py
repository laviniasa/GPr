# Faca um programa que preencha um vetor com os modelos de cinco carros (exemplos de
# modelos: Fusca, Gol, Vectra, etc.). Preencha outro vetor com o consumo desses carros,
# isto  ́e, quantos quilometros cada um deles faz com um litro de combustıvel. Calcule e
# mostre:
# (a) O modelo de carro mais economico;
# (b) Quantos litros de combust ́ıvel cada um dos carros cadastrados consomem para
# percorrer uma dist ˆancia de 1.000 quilometro


modelos = []
consumo = []
n = 0
while n != 2:
    m = str(input('  digite o modelo do carro'))
    modelos.append(m)
    c = int(input('  quantos quilometros ele faz com um litro de combustivel?'))
    consumo.append(c)
    n += 1
print(max(modelos))

