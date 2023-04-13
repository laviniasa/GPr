# Faca um programa que leia um numero inteiro positivo n
# e calcule a soma dos n primeiros
# numeros naturais

# n = 10
# count = 0
# for num in range(0, n):
#     count = count + 1
#     result = count + num
# print(result)


# n=int(input("Digite um número: "))
# soma = 0
# if n > 0:
#   for i in range(n+1):
#     soma = soma + i
#     print("para n = ",i," a soma é: ", soma)
#   print("Pronto! A soma dos ",n," primeiros números naturais é: ",soma)
# elif n < 0:
#   print("Somente para números positivos!")
  
  
v = []
n = int(input("Digite o valor de n: "))
if n -1 < 0:
    print('numero inválido')
count = 0
for num in range(1, n):
    if num % 2 != 0:
        v.append(num)
        v.sort()
        v.reverse()
print(v)