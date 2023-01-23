#- Faça uma função que recebe por parâmetro um valor X em segundos
#  e retorna esse tempo em horas, minutos e segundos.

def funcao(x):
    tempo_h = (x / 3600) 
    tempo_m = (x / 60) 
    tempo_s = (x)
    return tempo_h, tempo_m, tempo_s

v = 10000

test = funcao(v)
print(test)    