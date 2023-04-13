# Escreva um algoritmo que leia um n  ́umero inteiro entre 100 e 999 e imprima na sa ́ıda
# cada um dos algarismos que comp  ̃oem o n  ́ume


n = int(input("Digite o valor de n: "))
for i in range(100, n+n, 999):
   print(i)


# while True:
#    a = (int(input('insira um numero entre 100 e 999')))
#    if a < 100 or a > 999:
#        a = (int(input('insira um numero entre 100 e 999')))
#    if a > 100 and a < 999:
#        break
# b = str(a)

# for i, v in enumerate(b):

#    print(v)