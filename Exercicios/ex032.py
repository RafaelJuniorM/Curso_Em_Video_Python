# Desenvolva um programa que leia o comprimento de três retas 
# e diga ao usuário se elas podem ou não formar um triângulo.

lado_1 = int(input("Digite o comprimento do primeiro lado: "))
lado_2 = int(input("Digite o comprimento do segundo lado: "))
lado_3 = int(input("Digite o comprimento do terceiro lado: "))

if lado_1 + lado_2 > lado_3 and lado_1 + lado_3 > lado_2 and lado_2 +lado_3 > lado_1:
    print(" \n Os lados podem formar um triângulo.")
else:
    print("\n Os lados não podem formar um triângulo.")
