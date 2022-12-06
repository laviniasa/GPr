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