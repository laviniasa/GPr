# Construa um programa que leia duas strings fornecidas pelo usuario e verifique se a se-
# gunda string lida esta contida no final da primeira, retornando o resultado da verificacao

s1 = 'lavinialavinia'
s2 = 'lavinia'

result = s1.find(s2, len(s1) - len(s2))             
print(result)
