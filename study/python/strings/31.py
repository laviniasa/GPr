# Leia duas cadeias de caracteres A e B. Determine quantas vezes a cadeia A ocorre na
# cadeia B

a = '*'
b = '*n*'
count = 0

for letra in b:
    if letra == a:
        count = count + 1
print (count)