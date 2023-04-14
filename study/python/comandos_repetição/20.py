# Ler uma sequencia de numeros inteiros
# e determinar se eles sao pares ou n  ̃ao.
# Devera ser informado o numero de dados lidos e numero de valores pares. 
# O processo termina
# quando for digitado o n  ́umero 100

a = [1,2,3,4,5]
print(len(a))
v = []
for num in a:
    if num % 2 == 0:
        v.append(num)
        print(len(v))
    elif num == 100:
        break
        



# par = []
# v = []
# for i in range(4):
#     result = input('digite um valor: ')
#     if result == 100:
#         break
#     v.append(result)
# for num in v:
#     if (num % 2) == 0:
#         par.append(result)
#         print('é par')
#     else:
#         print('não é par')
# print(len(v))
# print(len(par))