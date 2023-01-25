# Classe Quadrado: Crie uma classe que modele um quadrado:
#    - Atributos: Tamanho do lado
#    - Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;

class Square:
    def __init__(self, lado="0"):
        self.lado = lado

    def valorLado(self, lado):
        self.lado = lado
        return self.lado

    def mudarLado(self, mudar):
        self.mudar=mudar

    def calcArea(self, lado):
        self.area=float(lado)*2
        return self.area

lado=(input("informe o valor:"))

um=Square(lado)


print(f" o valor da area é: {um.calcArea(lado)}")

square=Square(lado)