# 8. Faca um programa que conte o numero de 1’s que aparecem em um string. Exemplo:
# 0011001 -> 3

# def program(s):
#     count = 0
#     for n in s:
#         if n == 1:
#             count = count + 1
#     return count

# x = "00001111321"
# print(program(x))

x = "00001111321"
count = 0
for n in x:
    if n == 1:
        count = count + 1
    print (count)

