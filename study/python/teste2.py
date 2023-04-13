i = []
n = []
r = []
mini = []
pres = []

for q in range(2):
    nome = input('digite um nome: ')
    a = nome.capitalize().replace(" ", "-").strip()
    n.append(a)
    idade = input('digite sua idade: ')
    result = int(float((idade)))
    i.append(result)
    
    renda = input('digite sua renda: ')
    rendaf = float(renda)
    r.append(rendaf)
    
    imovel = float(input('digite o valor do imovel: '))
    financiamento = int(input('quantos anos de financiamento: '))
    minimo = rendaf * 30 / 100
    mini.append(minimo)
    prestacao = imovel / (financiamento * 12)
    pres.append(prestacao)

new_name = input('digite outro nome: ')
b = new_name.capitalize().replace(" ", "-").strip()
for count, pessoa in enumerate(n):
    if b == pessoa:
        print('pessoa encontrada')
        print(b, i[count])
        if i[count] <= 18:
            if pres[count] <= mini[count]:
                print('empréstimo aprovado')
            else:
                print('emprestimo negado')
        else:
                print('emprestimo negado')

    elif pessoa.startswith(b):
        print('mesmo nome encontrado')
        print(pessoa, i[count])
    
    elif pessoa.endswith(b):
        print('mesmo sobrenome')
        print(pessoa, i[count])
        
    # else:
    #     print('pessoa não encontrada')
        

