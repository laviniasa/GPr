# Fac ̧ a programas para calcular as seguintes sequencias:
# 1 + 2 + 3 + 4 + 5 + ... + n
# 1 −2 + 3 −4 + 5 + ... + (2n −1)
# 1 + 3 + 5 + 7 + ... + (2n −1)

def factorial(n):
    factorial = 1
    for i in range(n):
        factorial *= i+ 1
    return factorial

for i in range(10):
    print(factorial(i))















