class Carro:
    def __init__(self,consumo,quantidade):
        self.consumo=consumo
        self.quantidade=quantidade
    
    def andar(self,andar):
        self.quantidade-=(andar/consumo)
        
    def obterGasolina(self):
        return self.quantidade
        
    def adicionarGasolina(self,adicionarGasolina):
        self.quantidade+=adicionarGasolina

        
consumo = float(input("Digite o valor do consumo de gasolina: "))
quantidade = float(input("digite quantidade:"))    



mustang = Carro(consumo, quantidade) 
mustang.adicionarGasolina(20)
mustang.andar(100)            
print("quantidade de gasolina" +str (mustang.obterGasolina()))