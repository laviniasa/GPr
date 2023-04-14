# Faca um programa que calcule e mostre a soma dos 50 primeiros numeros pares
# soma = 0 
# count = 0
soma = 0
count = 0
for c in range(1,7):
    num = int(input("digite um valor: "))
    if num % 2 == 0:
        soma += num
        count += 1
print('{} numeros pares e a soma foi {}' .format(count, soma))
 
# while count < 50:
#     count += 1
#     soma += count * 2
# print(soma)

# pares = []
# count = 0
# soma = 0
# for num in range(0,5):
#     if num % 2 == 0:
#         pares.append(num)
# for n in pares:
#     count += 1
#     soma += count * 2
# print(soma)

        