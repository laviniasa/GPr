class Carro:
    def __init__(self, cor, combustivel=0, velocidade=0):
        self.cor = cor
        self.combustivel = combustivel
        self.velocidade = velocidade
    def aumentar_velocidade(self):
        self.velocidade += 10
        self.combustivel -= 5
    def diminuir_velocidade(self):
        self.velocidade -= 10
    def abastecer(self, valor):
        self.combustivel += valor
    def verifica_velocidade(self):
        return self.velocidade
    def verifica_combustivel(self):
        return self.combustivel
if __name__ == "__main__":
    cor = input("digite seu nome: ")
    carro = Carro(cor)
    escolha = ""
    while escolha != "c":
        print("1 - abastecer\n2 - aumentar velocidade\n3 - diminuir")
        print("4 - verifica velocidade\n5 - verifica combustivel")
        print("c - Cancelar")
        escolha = input("Digite a sua escolha: ")
        if escolha == "1":
            valor = float(input("Quanto vai abastecer? "))
            carro.abastecer(valor)
        elif escolha == '2':
            print("Velocidade aumentada")
            carro.aumentar_velocidade()
        elif escolha == '3':
            print("Velocidade diminuida")
            carro.diminuir_velocidade()
        elif escolha == '4':
            print(carro.verifica_velocidade())
        elif escolha == '5':
            print(carro.verifica_combustivel())
    print("Programa finalizado!")