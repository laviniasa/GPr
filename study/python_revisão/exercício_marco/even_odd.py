#1.5 - Uma função deve retornar, para cada número a informação: “Impar”, ou “Par”

def even_odd(n):
    list1 = n 
    result = ""
    even_count, odd_count = 0, 0
    for num in list1:  
        if num % 2 == 0: 
            even_count += 1
            result += str(num) +" Par "
        else: 
            odd_count += 1
            result += str(num) + " Impar "
    return result
x = [1,2,3,4,5,6,7,8,9,10]
teste = even_odd(x)
print(teste)
