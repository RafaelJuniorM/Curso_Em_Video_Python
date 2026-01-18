# Faça um programa que leia a largura e altura de uma parede em metros, calcule a sua area 
# e a quantidade de tinta necessário para pinta-la, sabendo que cada litro de tinta pinta uma área de 2m².

largura_parede = float(input("Digite a largura da parede em metros: "))
altura_parede = float(input("Digite a altura da parede em metros: "))

area_total_parede = altura_parede*largura_parede
quantidade_tinta_necessario = area_total_parede/2

print(f"A área total da parede é {area_total_parede} m².")
print(f"A quantidade de tinta necessária para pintar a parede é {quantidade_tinta_necessario} litros.")