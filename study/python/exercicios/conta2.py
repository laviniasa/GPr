class ContaCorrente:

    def __init__(self,numero_conta, nome_correntista,saldo=0):
        self.saldo = saldo
        self.numero_conta = numero_conta
        self.nome_correntista = nome_correntista

    def alterar_nome(self, novo_nome):
        self.nome_correntista = novo_nome
        return self.nome_correntista

    def deposito(self,valor_deposito):
        self.saldo += valor_deposito
        return self.saldo

    def saque(self,valor_saque):
        self.saldo -= valor_saque
        return self.saldo

if __name__ == "__main__":
    conta_corrente = ContaCorrente(250,'Lavinia')

    nome = input('Digite seu nome: ')

    print (conta_corrente.__dict__)
    escolha = 0
    while escolha <4 :
        escolha = float(input(' escolha uma opção: 1 - Alterar nome, 2 - Deposito, 3 - Salque, 4 - cancelar: '))
        print('')
        if escolha == 1:
            novo_nome = input('Digite seu nome: ')
            conta_corrente.alterar_nome(novo_nome)
            print (conta_corrente.__dict__)
        elif escolha == 2:
            valor = float(input("Quanto vai Depositar? "))
            conta_corrente.deposito(valor)
            print (conta_corrente.__dict__)
        elif escolha == 3:
            valor = float(input("Quanto vai Sacar? "))
            conta_corrente.saque(valor)
            print (conta_corrente.__dict__)
        else:
            break