class Filme:

   def __init__(self, nome: str, classificacao: int):

       self.nome = nome

       self.classificacao = classificacao

   def cadastrar():

       print("_____ Cadastrar Filme _____")

       nome = input("Digite o nome do filme: ")

       classificacao = input("Digite a faixa etária: ")

       print("_____ *************** _____")

       return Filme(nome, int(classificacao))

class Pessoa:

   def __init__(self, nome: str, idade: int):

       self.nome = nome

       self.idade = idade

   def cadastrar_pessoas(c: int):

       idade = -1

       pessoas = []

       print("_____ Cadastrar Pessoas _____")

       for _ in range(c):

           nome = input("Digite o nome: ")

           idade = input("Digite a idade: ")

           if idade != 0:

               pessoas.append(Pessoa(nome, int(idade)))

           else:

               break

       print("_____ *************** _____")

       return pessoas

class Sala:

   def __init__(self, nome_sala: str, capacidade: int):

       self.nome = nome_sala

       self.capacidade = capacidade

   def cadastrar():

       print("_____ Cadastrar Sala _____")

       nome = input("Digite o nome: ")

       capacidade = input("Digite a capacidade: ")

       print("_____ *************** _____")

       return Sala(nome, int(capacidade))

class Cinema:

   def __init__(self, salas: [Sala], filmes: [Filme], pessoas: [Pessoa]):

       self.salas = salas

       self.filmes = filmes

       self.pessoas = pessoas

   #* O nome do Filme, sala em que será exibido e o seu tamanho e a classificação etária do mesmo;

   def print_a(self, indx_filme = 0, indx_sala = 0):

       print(f"O nome do filme é: {self.filmes[indx_filme].nome}, sala: {self.salas[indx_sala].nome}, capacidade: {self.salas[indx_sala].capacidade} pessoas, classificação: {self.filmes[indx_filme].classificacao} anos.")

   #* O número de pessoas e o percentual de ocupação da mesma; não deve exceder o tamanho/capacidade da sala;    

   def print_b(self, indx_sala = 0):

       qtd_pessoas = len(self.pessoas)

       perc_ocup = round((qtd_pessoas/self.salas[indx_sala].capacidade) * 100, 2)      

       print(f"Quantidade de pessoas: {qtd_pessoas}, percentual de ocupação: {perc_ocup}%")

   #* O nome de cada pessoa com a sua idade e a informação se atende a faixa etária do filme;

   def print_c(self, indx_filme = 0):    

       for p in self.pessoas:

           if p.idade >= self.filmes[indx_filme].classificacao:

               print(f"{p.nome} está dentro da faixa etária.")

           else:

               print(f"{p.nome} está fora da faixa etária.")

   #* A idade média do grupo; A menor idade e a maior idade.

   def print_d(self):

       idades = [p.idade for p in self.pessoas]

       media = round(sum(idades)/len(idades), 1)

       menor_idade = min(idades)

       maior_idade = max(idades)

       print(f"A média das idades é: {media}, a menor idade é: {menor_idade}, a maior idade é {maior_idade}.")

   def exibir_relatorio(self, indx_filme = 0, indx_sala = 0):

       self.print_a()

       self.print_b()

       self.print_c()

       self.print_d()

def teste_cinema():

   filme = Filme.cadastrar()

   sala = Sala.cadastrar()

   pessoas = Pessoa.cadastrar_pessoas(sala.capacidade)

   cinema = Cinema([sala], [filme], pessoas)

   cinema.exibir_relatorio()

def main():

   teste_cinema()

if __name__ == "__main__":

   main()