from random import randint  
itens = ('Pedra','Papel','Tesoura')
computador = randint(0, 2)
print('''Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
jogador = int(input('Qual é a sua jogada'))
print('computador jogou {}'.format(itens[computador]))
print('jogador jogou {}'.format(itens[jogador]))
if computador == 0:
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCEU =)')
    elif jogador == 2:
        print('COMPUTADOR VENCEU :(')
else:
    print('')

if computador == 1:
    if jogador == 0:
        print('COMPUTADOR VENCEU :(')
    elif jogador == 1:
        print('EMPATE)')
    elif jogador == 2:
        print('JOGADOR VENCEU :(')
else:
    print('')

if computador == 2:
    if jogador == 0:
         print('JOGADOR VENCEU :(')
    elif jogador ==1:
        print('COMPUTADOR VENCEU :(')
    elif jogador ==2:
         print('EMPATE)')
else:
    print('')