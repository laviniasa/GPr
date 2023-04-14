# Faca um programa que leia 10 inteiros positivos, ignorando nao positivos, e imprima sua
# media.

soma = 0
i = 0
while i < 10:
   v = int(input("digite um valor: "))
   if v > 0:
       soma = soma + v
       media = soma / 10
       i = i + 1
   else:
       print("digite um valor positivo")
print(media)






# v = []
# count = 0
# for i in range(10):
#     result = int(input('digite um valor: '))
#     count += 1
#     if result >= 0:
#         v.append(result)
#         print(v)
# for num in v:
#     x = (num + count) / 2
# print(x)
        