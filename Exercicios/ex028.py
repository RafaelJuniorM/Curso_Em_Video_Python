# Desenvolva um programa que pergunte a distancia de uma viagem em KM.
#  Calcule o preço da passagem, cobrando R$0,50 por KM para viagens de até 200KM e R$0,45 para viagens mais longas.
distancia_viagem = int(input("Digite a distancia da sua viagem em km: "))

if distancia_viagem <= 200:
    preco_passagem = distancia_viagem * 0.50
    print(f"O preço da sua passagem será de R$ {preco_passagem:.2f}")
else:
    preco_passagem = distancia_viagem * 0.45
    print(f"O preço da sua passagem será de R$ {preco_passagem:.2f}")

print("Boa viagem!")