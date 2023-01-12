#-     Classe Retangulo: Crie uma classe que modele um retangulo:
#    - Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
#    - Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;
#      Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as medidades de um local. Depois, deve criar um objeto com as medidas e calcular a quantidade de pisos e de rodapés necessárias para o local.

class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura
    
    def perimetro(self):
        return (2*self.base) + (2*self.altura)

base = float(input("Digite o valor da base: "))
altura = float(input("Digite o valor da altura: "))

retangulo = Retangulo(base, altura)
area = retangulo.area()
perimetro = retangulo.perimetro()

print(f"A quantidade de pisos necessários é {area} metros quadrados e a quantidade de rodapés necessários é de {perimetro} metros lineares")