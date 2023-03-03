# Faça um Programa que leia um número e exiba o dia correspondente da semana. 
#(1- Domingo , 2- Segunda, etc.) se digitar outro valor deve aparecer “valor inválido)0n +99
# digitar um numero 

# comparar - se o numero for igual a 1 - mostra domingo

# o mesmo para os outros dias

# agora se digitar outro valor deve aparecer “valor inválido"

numero = input('Digite um numero:')

if numero == '1':
    print ('1-Domingo')
    
elif numero == 2:
    print ('2-Segunda')
    
elif numero == 3:
    print ('3-Terça')
    
elif numero == 4:
    print ('Quarta')
    
elif numero == 5:
    print ('5-Quinta')
    
elif numero == 6:
    print ('6-Sexta')
    
elif numero == 7:
    print ('7-Sabádo')
    
else:
    print ('entrada invalida')