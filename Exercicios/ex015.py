# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi 
# alugado. calcule o preço a pagar, sabendo que o carro custa r$ 60 por dia e R$0,15 por Km rodado.

km_rodado = float(input("Informe quantos km foram percorridos:  "))
dias_alugados = int(input("Total de dias que o carro foi alugado:"))

total_pagar = (60*dias_alugados) + (0.15*km_rodado)

print(f"O total a pagar pelo aluguel do carro é de R$ {total_pagar:.2f}")