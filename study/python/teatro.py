class Teatro:
    def _init_(self, capacidade_max = 30, ingresso = 0, lugares_vagos=30):
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
        print("_ Menu _")
        print("digite 1 para comprar ingressos")
        print("digite 2 para ver total da compra")
        print("digite 3 para ver lugares disponíveis")
        print("digite 4 para ver total arrecadado")
        print("digite 5 para sair")
    
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
       
if _name_ == "_main_":

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
            print("_ Cliente: _")
            nome = input("Digite o nome: ")

            print('')

            print("_ ingressos _")       
            bilhete = int(input('que tipo de ingresso? (1-inteira/2-meia): '))
            
            print('')

            print("_Lugares_")
            Zenaide.exibir()
            
            print('')
            
            lugares = input("escolha uma opção de lugar:")
            linha, coluna = lugares.split(',')
            reserva = Zenaide.reserva(int(linha), int(coluna))
            if reserva == True:
                resp = str(input('mais ingressos? (y/ n): ')).lower()
            else:
                lugares = input("escolha uma opção de lugar:")
                
            if resp == 'n':
                resp = str(input('qual é a forma de pagamento?(1- Débito/ 2- Crédito ): ')).lower()
                if resp != 3:
                   senha = int(input('digite sua senha:  '))
                   print('pagamento efetuado')
                   resp = str(input('ver menu? ( y/n): ')).lower()
                   
            if bilhete == 1:
            # print(inteira)
                total = 40
            else:
                #print(meia)
                total = 20
                print(total)
        elif opcao == 2:
            print(total)
            resp = str(input('ver menu? ( y/n): ')).lower()
            if resp == "y":
                Zenaide.menu()
                opcao = int(input("digite sua escolha"))
            else:
                break
        
        elif opcao == 3:
            Zenaide.exibir()
            resp = str(input('ver menu? ( y/n): ')).lower()
            if resp == "y":
                Zenaide.menu()
                opcao = int(input("digite sua escolha"))
            else:
                break
        
            
        elif opcao == 4:
            print("_ Total Arrecadado: _")
            print(total_geral)
            if resp == "y":
                Zenaide.menu()
                opcao = int(input("digite sua escolha"))
            else:
                break
        
        elif opcao == 5:
            break
        else:
            print("opção invalida")
            print('')
            if resp == "y":
                Zenaide.menu()
                opcao = int(input("digite sua escolha"))
            else:
                break
        
        total_geral += total
