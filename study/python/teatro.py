class Teatro:
    def __init__(self, capacidade_max = 30, ingresso = 0, lugares_vagos=30):
        self.capacidade_max=capacidade_max
        self.ingresso=ingresso
        self.total_arrecadado = 0
        self.lugares_vagos=lugares_vagos
        self.poltronas = [
            ["[0,0]", "[0,1]", "[0,2]", "[0,3]", "[0,4]"],
            ["[1,0]", "[1,1]", "[1,2]", "[1,3]", "[1,4]"],
            ["[2,0]", "[2,1]", "[2,2]", "[2,3]", "[2,4]"],
            ["[3,0]", "[3,1]", "[3,2]", "[3,3]", "[3,4]"],
            ["[4,0]", "[4,1]", "[4,2]", "[4,3]", "[4,4]"]
        ]

    def exibir(self):
        for linha in self.poltronas:
            for lugar in linha:
                print(lugar, end=" ")
            print("")

    def menu(self):
        print("__ Menu __")
        print("digite 1 para opção venda dos ingressos")
        print("digite 2 ver total da compra")
        print("digite 3 para opção ver lugares")
        print("digite 4 para opção ver total arrecadado")
        print("digite 5 para opção sair")
    
    def reserva(self, x, y):
        if self.poltronas[x][y] != "[X]":
            self.poltronas[x][y] = "[X]"
            print ("lugar vago")
            
            return True
        else:
            print('lugar ocupado')
            return False

    def final (self, total_arrecado):
        self.final+=total_arrecado
       
if __name__ == "__main__":

    Zenaide = Teatro()
    Zenaide.menu()
    opcao = int(input("digite sua escolha  "))
    
    print(opcao)
    
    inteira = 40
    meia = 20
    total = 0
    total_geral = 0
    bilhete=0
    resp = 'y'
    teste = 0

    while opcao != 5:
        if opcao == 1:
            print("__ Cliente: __")
            nome = input("Digite o nome: ")

            print('')

            print("_ ingressos _")       
            bilhete = int(input('que tipo de ingresso? (1-inteira/2-meia): '))
            
            print('')

            print("__Lugares__")
            Zenaide.exibir()
            
            print('')
            
            lugares = input("escolha uma opção de lugar:")
            linha, coluna = lugares.split(',')
            Zenaide.reserva(int(linha), int(coluna))
            resp = str(input('mais ingressos? (1- y/ 2- n): ')).lower()
            if resp == 'n':
                resp = str(input('qual é a forma de pagamento?(1- Débito/ 2- Crédito ): ')).lower()
                if resp != 3:
                   senha = int(input('digite sua senha:  '))
                   print('pagamento efetuado')
                   lugares = int(input('voltar ao menu? (1-y/2-n): '))
                   if lugares == 1:
                    Zenaide.menu()
                    opcao = int(input("digite sua escolha  "))
    
                    
                
            if bilhete == 1:
            # print(inteira)
                total = 40
            else:
                #print(meia)
                total = 20
                print(total)
        elif opcao == 2:
            print(total)
            resp = str(input('ver menu? (1- y/ 2- n): ')).lower()
            resp == 1
            Zenaide.menu()

            opcao = int(input("digite sua escolha"))
        
        elif opcao == 3:
            Zenaide.exibir()
            lugares = int(input('voltar ao menu? (1-y/2-n): '))
            lugares == 1
            Zenaide.menu()
            
        elif opcao == 4:
            print("__ Total Arrecadado: __")
            print(total_geral)
            bala = int(input('voltar ao menu? (1-y/2-n): '))
            if bala == 1:
                Zenaide.menu()
            else:
                bala == 2
                break
        elif opcao == 5:
            break
        else:
            print("opção invalida")
            print('')
            lugares = int(input('voltar ao menu? (1-y/2-n): '))
            lugares == 1
            Zenaide.menu()
            opcao = int(input("digite sua escolha  "))
        total_geral += total
