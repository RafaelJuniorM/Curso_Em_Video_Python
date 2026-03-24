# Faça um programa que leia 5 valores numericos e guarde-os em uma lista. 
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

valores = []

for contador in range(0, 5):
    valores.append(int(input(f"Digite o valo na posição {contador}: ")))

print("-="*30)
print(f"Você digitou os valores {valores}")
print(f"O maior valor digitado foi {max(valores)} nas posições ", end="")
for indice, valor in enumerate(valores):
    if valor == max(valores):
        print(f"{indice}...", end="")
print()       

print(f"O menor valor digitado foi {min(valores)} nas posições ", end="")
for indice, valor in enumerate(valores):
    if valor == max(valores):
        print(f"{indice}...", end="")
print()   


# Outro forma de validar se um numero é maior ou menor:
#   if contador == 1: #       
#       maior = menor = numero 
#  else:
#       if numero > maior:
#            maior = numero 
#       if numero < menor:
#            menor = numero