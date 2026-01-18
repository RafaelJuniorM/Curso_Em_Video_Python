# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dolares ela pode comprar. 

seu_dinheiro = float(input(" Quanto voce possui na sua carteira: R$ "))

seu_dinheiro_dolar = seu_dinheiro / 5.37 

print(f"Com R$ {seu_dinheiro:.2f} voce pode comprar U$ {seu_dinheiro_dolar:.2f} ")