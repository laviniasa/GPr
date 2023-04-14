# Escreva um algoritmo que leia um n  ́umero inteiro entre 100 e 999 e imprima na sa ́ıda
# cada um dos algarismos que compoem o numero



numero = int(input("digite um número: "))

while(numero < 100 or numero > 999):

   print('número invalido')

   numero = int(input("digite um número: "))

centenas = numero//100

dezenas = (numero - centenas*100)//10

unidades = numero - (centenas*100 + dezenas*10)

print(f'O número {numero} é igual a {centenas*100} + {dezenas*10} + {unidades}')


# n = int(input("Digite o valor de n: "))
# for i in range(100, n+n, 999):
#    print(i)


# while True:
#    a = (int(input('insira um numero entre 100 e 999')))
#    if a < 100 or a > 999:
#        a = (int(input('insira um numero entre 100 e 999')))
#    if a > 100 and a < 999:
#        break
# b = str(a)

# for i, v in enumerate(b):

#    print(v)