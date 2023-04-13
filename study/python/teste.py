i = []
n = []
for q in range(2):
    nome = input('digite um nome: ')
    a = nome.capitalize().replace(" ", "-").strip()
    n.append(a)
    idade = input('digite sua idade: ')
    result = int(float((idade)))
    i.append(result)
    
new_name = input('digite outro nome: ')
b = new_name.capitalize().replace(" ", "-").strip()
for count, pessoa in enumerate(n):
    if b == pessoa:
        print('pessoa encontrada')
        print(b, i[count])
    elif pessoa.startswith(b):
        print('mesmo nome encontrado')
        print(pessoa, i[count])
    elif pessoa.endswith(b):
        print('mesmo sobrenome')
        print(pessoa, i[count])
    # else:
    #     print('pessoa não encontrada')
        


