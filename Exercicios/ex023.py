# Faça um programa que leia um numero de 0 a 999 e mostre na tela cada um dos digitos separados.
# # Exemplo: Digite um numero: 1834
# Unidade: 4
# Dezena: 3
# Centena: 8
# Milhar: 1

numero = input("Digite um numero de 0 a 9999: ")
numero = numero.zfill(4)

print(f"O numero: {numero}")
print(f"Unidade: {numero[-1]}")
print(f"Dezena: {numero[-2]}")
print(f"Centena: {numero[-3]}")
print(f"Milhar: {numero[-4]}")