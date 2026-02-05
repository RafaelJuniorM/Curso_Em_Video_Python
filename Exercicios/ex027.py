# Crie um programa que leia um numero inteiro e mostre na tela se ele é PAR ou ÍMPAR.

numero = int(input("Digite um valor: "))

validadando_numero = numero % 2
if validadando_numero == 0:
    print(f"O numero {numero} é PAR")
else:
    print(f"O numero {numero} é ÍMPAR")