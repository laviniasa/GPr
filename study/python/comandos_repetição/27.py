# Em Matem  ́atica, o n  ́umero harm ˆonico designado por H(n) define-se como sendo a soma
# da s  ́erie harm  ́onica:
# H(n) = 1 + 1/2 + 1/3 + 1/4 + ... + 1/n

n = int(input("Informe o N"))
soma = 0
for i in range(1,n+1):
    soma += 1/i
print("a soma harmonica é",soma)
