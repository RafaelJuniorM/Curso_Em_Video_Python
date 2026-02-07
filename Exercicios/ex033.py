# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. 
# O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar. 
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.

valor_casa = float(input("Digite o valor da casa: R$ "))
valor_salario = float(input("Digite o seu salario: R$ "))
anos_pagando = int(input("Em quantos anos voce vai pagar: "))

valor_mensal  = valor_casa / (anos_pagando * 12)

if valor_mensal > (valor_salario * 0.3):
    print(f"\n Empréstimo negado! O valor da prestação mensal de R${valor_mensal:.2f}excede 30% do seu salário.")
else:
    print(f"\n Empréstimo aprovado! O valor da prestação mensal de R${valor_mensal:.2f} está dentro do limite permitido.")
