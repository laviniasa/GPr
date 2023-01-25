from random import randint

print('vou pensar em um numero entre 0 e 10, tente adivinhar....')

computador = randint(0, 10)
cont = 0

while cont<3:
    jogador = int(input('Em que numero eu pensei?'))
   # rodada = 1
    if jogador == computador:
        if cont == 0:
            print('nota maxima 100')
            break
        elif cont == 1:
             print('50 pontos')
             break
        elif cont == 2:
            print(' sua pontuação é 25')
        print('PARABÉS VOCÊ ACERTOU! =))))')
   #rodada = 2
    else:
        if cont < 2:
            print('tente de novo')
        else:
            print('perdeu!')
    cont = cont +1
print('fim')

        
        
    
    

   