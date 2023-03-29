# 13. Faca um programa que receba uma palavra e calcule quantas vogais (a, e, i, o, u) 
# possui essa palavra. Entre com um caractere (vogal ou consoante) e substitua todas as
# vogais da palavra dada por esse caractere.


vogais = 'aeiou'
s = 'vinicius'
qtd_vogais = 0
for v in s.lower():
    if v in vogais:
        qtd_vogais += 1   
        a = (s.replace(vogais, "*"))

print(a) # 5


a = 'lavinia'
b = 'aeiou'
for letra in range(0, len(b)):
    a = a.replace(b[letra], "")
print(a)
