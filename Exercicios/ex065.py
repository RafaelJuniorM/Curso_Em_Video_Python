# crie um programa que leia o nome e o preço de varios produtos. O programa deverá perguntar se o usuario vai continuar ou nao.
#  No final, mostre:
# A) Qual é o total gasto na compra.
# B) Quantos produtos custam mais de R$1000.
# C) Qual é o nome do produto mais barato.

qtd_produtos = 0

from time import sleep
total_gasto = produto_acima_mil = produto_mais_barato =  0
nome_produto_mais_barato = ''

print("-="*30)
print(" "*20+"CADASTRO DE PRODUTOS ")
print("-="*30)

while True:
    produto = str(input("Informe o nome do produto: ")).strip().upper()
    preco_produto = input("Informe o preço do produto: R$ ").replace(",",".")

    preco_produto = float(preco_produto)
    
    qtd_produtos += 1
    # A) Qual é o total gasto na compra.
    total_gasto += preco_produto

    # B) Quantos produtos custam mais de R$1000.
    if preco_produto > 1000:
        produto_acima_mil += 1

    # C) Qual é o nome do produto mais barato.
    if qtd_produtos == 1 or preco_produto < produto_mais_barato:
        produto_mais_barato = preco_produto
        nome_produto_mais_barato = produto

    print(f"Nome do produto: {produto} \n Preço do produto: R$ {preco_produto}")
    sleep(1)
    print("-="*30)
    print("CADASTRANDO ...")
    sleep(1)
    print("~"*30)
    print("Produto cadastrado com sucesso!!!")
    print("~"*30)

    deseja_continuar = ' '
    while deseja_continuar not in "SN":
        print("Resposta invalida, tente novamente!")
        deseja_continuar = str(input("Deseja continuar cadastrando produtos? [S/N]: ")).strip().upper()[0]
    
    if deseja_continuar == "N":
        print("-="*30)
        print("Cadastro encerrado, volte sempre!")
        break

print(f" Total gasto na compra: R$ {total_gasto:.2f}")
print(f" Quantidade de produtos acima de R$ 1000: {produto_acima_mil}")
print(f" O produto mais barato é {nome_produto_mais_barato} com o preço de R$ {produto_mais_barato:.2f}")