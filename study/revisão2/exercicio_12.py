# Faça um programa que leia e valide as seguintes informações:
# Nome: maior que 3 caracteres;
# Idade: entre 0 e 150;
# Salário: maior que zero;
# Sexo: 'f' ou 'm';
# Estado Civil: 's', 'c', 'v', 'd';
# Use a função len(string) para saber o tamanho de um texto (número de caracteres).
# Inicialmente, pedimos as 5 informações ao usuário 
# (sempre informe como deve ser essa informação que ele deve fornecer,
#  o seu formato, para ele informar corretamente).

# Depois, vamos usando 5 loopings WHILE para nos certificar se ele forneceu 
# os dados corretos.

def program(a, b, c, d, e):
    while len(a) <= 3:
        a = input("Seu nome deve ter mais que 3 caracteres: ")

    while (b < 0) or (b > 150):
        b = int(input("Voce deve ter entre 0 e 150 anos: "))

    while (c<0):
        c = float(input("A coisa ta difícil, mas não tem salário negativo: "))

    while (d!= 'f') and (d!='m'):
        d = input("Biologicamente, você deve ser 'f' ou 'm': ")

    while (e!='s')and(e!='c')and(e!='v')and(e!='d'):
        print("Nao tem estado civil 'confuso'")
        e = input("Deve ser s, c, v ou d: ")
    else:
        print ('vc foi cadastrado')

        
        

nome = input("Qual seu nome [minimo 4 caracteres]: ")
idade = int(input("Sua idade: "))
salario = float(input("Salário: "))
sexo = input("Sexo ('f' para feminino ou 'm' para masculino): ")
civil = input("Estado civil (s, c, v ou d): ")

test = program(nome, idade, salario, sexo, civil)
print(test)

