# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triâgulo retângulo, 
# calcule e mostre o comprimento da hipotenusa.

import math

cateto_oposto = float(input("Informe o comprimento do cateto oposto:"))
cateto_adjancente = float(input("informe o comprimento do cateto adjacente: "))


hipotenusa = math.hypot(cateto_oposto, cateto_adjancente)
print(f"O comprimento da hipotenusa é de {hipotenusa:.2f}")
