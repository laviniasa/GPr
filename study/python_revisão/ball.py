#Classe Bola: Crie uma classe que modele uma bola:
#    - Atributos: Cor, circunferência, material
#    - Métodos: trocaCor e mostraCor

class Ball:
    def __init__ (self, cor, circunferencia, material):
        self.cor=cor
        self.circunferencia=circunferencia
        self.material=material

    def trocaCor(self, cor):
        self.cor=cor

    def mostraCor(self):
        return self.cor

cor = 'amarelo'
circunferencia= 5
material= 'plástico'

b = Ball(cor, circunferencia, material)
print(b.cor)

