class Bola:
    def __init__(self, cor, circunferencia, material):
        self.cor=cor 
        self.circunferencia=circunferencia
        self.material=material

    def trocaCor(self, cor):
        self.cor=cor

    def mostraCor(self):
        return self.cor

cor=(input("informe a cor da sua bola:"))
circunferencia=(input("informe a circunferencia da bola:"))
material=(input("informe o material da bola:"))

bola=Bola(cor,circunferencia,material)

print(f"sua bola {bola.cor} de {bola.material} com tamanho {bola.circunferencia} foi criada!")


    
