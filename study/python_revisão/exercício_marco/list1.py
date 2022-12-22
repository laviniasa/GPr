#2 - Ao receber duas sequência de números:
#2.1 - Uma função deve retornar, se for possível, a soma dos números como o exemplo a seguir:


def soma(n):
    D = [ (a + b) for a, b in zip(n)]

Seq1 = [1, 5, 9, 2]
Seq2 = [5, 10, 4, 9]

somar = soma(Seq1, Seq2 )
print(soma(somar))