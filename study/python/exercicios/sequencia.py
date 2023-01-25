soma=0
count=0

for c in range(1,7):
    num = int('digite o {} valor:'.format(c))
    if num % 2 == 0:
        soma+=num 
        count+= 1
    print('voce informou {} numeros e a soma foi {}'.format(count,soma))