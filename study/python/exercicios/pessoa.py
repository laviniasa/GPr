class Pessoa:
    def __init__(self, nome: str, idade: int, peso: float, altura: float):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self):
        if self.idade < 21:
            self.altura += 0.5

        self.idade += 1

    def engordar(self, peso):
        self.peso += peso

    def emagrecer(self, peso):
        self.peso -= peso

    def crescer(self, altura):
        self.altura += altura


    def mostraPessoa(self):
        print(f'Nome: {self.nome}, idade: {self.idade} anos, peso: {self.peso}kg, altura: {self.altura}cm')


lavinia = Pessoa('Lavinia', 18, 68, 152)
lavinia.mostraPessoa()
lavinia.envelhecer()
lavinia.emagrecer(15)
lavinia.engordar(2)
lavinia.mostraPessoa()
lavinia.envelhecer()
lavinia.emagrecer(15)
lavinia.mostraPessoa()
lavinia.engordar(2)