# faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preco_produto = float(input("Digite o preço do produto: R$  "))

desconto = 5/100 

valor_produto_descontado = preco_produto - (preco_produto * desconto)

print(f"Com desconto de 5% seu novo preço é R$ {valor_produto_descontado:.2f}")