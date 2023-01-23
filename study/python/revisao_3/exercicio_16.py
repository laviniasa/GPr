#- Faça um programa que receba um número e usando laços de repetição
#  calcule e mostre a tabuada desse número.

    
num = input("digite um numero")
tab = int(num)

for i in range(0,11):
    print (i, "*", tab, "=", i*tab)