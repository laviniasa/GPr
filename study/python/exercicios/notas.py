
if __name__ == "__main__":
    notas = [1, 2, 5, 10, 20,50]
    notas = reversed(notas)
    v = int(input("quanto deseja sacar?"))
    
    
    for nota in notas:
        if v > 0:
            qtd = int(v / nota)
            v = int(v - (qtd*nota))
            if qtd != 0:
                print (f" {qtd} notas de {nota}")
        else:
            break
        
