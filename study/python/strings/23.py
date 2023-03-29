# Ler o nome e o valor de uma determinada mercadoria de uma loja. Sabendo que o
# desconto para pagamento `a vista  ́e de 10% sobre o valor total, calcular o valor a ser
# pago `a vista. Escrever o nome da mercadoria, o valor total, o valor do desconto e o valor
# a ser pago `a vista


mercadoria = 'feijão' 
feijão = 50
valor_do_desconto = 10 / 100
a_pagar = float(feijão * valor_do_desconto)

print(mercadoria)
print("valor total%7.2f." % feijão)
print("desconto%7.2f." % valor_do_desconto)
print("O valor a pagar avista é de R$ %7.2f" % a_pagar)

