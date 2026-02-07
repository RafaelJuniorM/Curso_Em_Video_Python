# Escreva um programa que leia dois numero inteiro e compare-os, mostrando na tela uma mensagem:
# - O primeiro valor é maior
# - O segundo valor é maior

numero_1 = int(input("Digite o valor do primeiro numero: "))
numero_2 = int(input("Digite o valor do segundo numero: "))

if numero_1 > numero_2:
    print(f"\n o primeiro valor é MAIOR \n")

elif numero_2 > numero_1:
    print(f"\n o segundo valor é MAIOR \n")
else:
    print(f"\n os dois valores são IGUAIS \n")