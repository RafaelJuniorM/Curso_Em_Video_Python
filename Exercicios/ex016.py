# Crie um programa que leia um numero real qualquer pelo teclado e mostre na tela sua porção inteira. 
# Ex: Digite um numero: 6.127
# O numero 6.127 tem a parte inteira 6.

import math

numero = float(input("Digite um numero real: "))
print(f"O numero {numero} tem a parte inteira {math.trunc(numero)}")