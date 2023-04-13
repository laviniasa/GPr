# Escreva um programa completo
# que permita a qualquer aluno introduzir, pelo teclado, uma sequencia arbitraria de notas 
# (validas no intervalo de 10 a 20)
# e que mostre na tela, como resultado, a correspondente media aritmetica.
# O numero de notas com que o aluno pretenda efetuar o c  ́alculo nao sera fornecido ao programa,
# o qual terminara quando for introduzido um valor que n  ̃ao seja valido como nota de aprovac

notas = []
nota2 = []
a = 0 
while a == 0:
    r = int(input('digite sua primeira nota'))
    r2 = int(input('digite sua segunda nota'))
    notas.append(r)
    nota2.append(r2)
    media = (r + r2) /2
    if media >= 10 and media <=20:
        print('aprovado')
        print(media)
    else:
        print('reprovado')
    

