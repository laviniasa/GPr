#- Faça um Programa que leia um número e exiba o dia correspondente da semana.
#  (1- Domingo , 2- Segunda, etc.) se digitar outro valor deve aparecer “valor inválido)

dia_semana = int(input('Digite um número de (1 a 7): '))

if dia_semana == 1:
    print('-> Segunda')

elif dia_semana == 2:
    print('-> Terça')

elif dia_semana == 3:
    print('-> Quarta')

elif dia_semana == 4:
    print('-> Quinta')

elif dia_semana == 5:
    print('-> Sexta')

elif dia_semana == 6:
    print('-> Sabado')

elif dia_semana == 7:
    print('-> Domingo')

else:
    print('Dia não encontrado.')
