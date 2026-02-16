# Crie um programa que leia o ano de nascimento de sete pessoas
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores
from datetime import date


data = date.today().year
total_menor = 0
total_maior = 0

for pessoas in range(1,8):
    ano_nasc = int(input(f"Em que ano a {pessoas} nasceu ? "))
    idade = data - ano_nasc
    print(f"{idade}")
    if idade >= 18: 
        total_maior += 1
    else:
        total_menor += 1

print(f"O numero de pessoas maiores de idades é {total_maior} ")
print(f"O numero de pessoas menores de idades é {total_menor} ")