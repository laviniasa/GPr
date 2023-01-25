# Classe carro: Implemente uma classe chamada Carro com as seguintes propriedades:
# Um veículo tem um certo consumo de combustível (medidos em km / litro)
#  e uma certa quantidade de combustível no tanque.

#  O consumo é especificado no construtor e o nível de combustível inicial é 0.

#  Forneça um método andar( ) que simule o ato de dirigir 
# o veículo por uma certa distância, reduzindo o nível de combustível no tanque de gasolina.
# Forneça um método obterGasolina( ), que retorna o nível atual de combustível.
# Forneça um método adicionarGasolina( ), para abastecer o tanque.


# Exemplo de uso:
# meuFusca = Carro(15);           # 15 quilômetros por litro de combustível.
# meuFusca.adicionarGasolina(20); # abastece com 20 litros de combustível.
# meuFusca.andar(100);            # anda 100 quilômetros.
# meuFusca.obterGasolina()        # Imprime o combustível que resta no tanque.




# class Carro:
#     def __init__(self,consumo,combustível=0):
#         self.consumo=consumo
#         self.combustível=combustível
    
#     def andar(self,andar):
#         self.combustível-=(andar/consumo)
        
#     def obterGasolina(self):
#         return self.combustível
        
#     def adicionarGasolina(self,adicionarGasolina):
#         self.combustível+=adicionarGasolina

# if __name__ == "__main__":
    
#     carro = Carro()

#     escolha = ""
#     while escolha != "c":
#         print("1 - abastecer\n2 - andar")
#         print("3 - combustivel inicial")
#         print("c - Cancelar")

#         escolha = input("Digite a sua escolha: ")

#         if escolha == "1":
#             valor = float(input("Quanto vai abastecer? "))
#             combustível = float(input("digite a quantidade de combustível:"))    
#             carro.adicionarGasolina(20)
            

#         elif escolha == '2':
#             print("o carro está em movimento")
#             carro.andar(100) 

            
#         elif escolha == '3':
#             print(carro.obterGasolina())
#             print(carro)

#         print("Programa finalizado!")

class Carro:
    def __init__(self,consumo,combustivel=0):
        self.consumo=consumo
        self.combustivel=combustivel
    
    def andar(self,andar):
        self.combustivel-=(andar/consumo)
        
    def obterGasolina(self):
        return self.combustivel
        
    def adicionarGasolina(self,valor):
        self.combustivel+=valor

consumo = float(input("Digite o valor do consumo de gasolina: "))
combustivel = float(input("digite combustivel:"))    
mustang = Carro(consumo, combustivel) 
mustang.adicionarGasolina(20)
mustang.andar(100)            
print("combustivel de gasolina" +str (mustang.obterGasolina()))