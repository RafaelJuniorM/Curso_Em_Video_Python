# Crie um algoritmo que leia um numero e mostre o seu dobro, triplo e raiz quadrada. 

numero = int(input("Digite um numero: "))

numero_dobro = numero*2
numero_triplo = numero*3
numero_raiz_quadrada = numero**(1/2)

print(f"Seu numero ´r: {numero}")
print(f"O dobro de seu numero é: {numero_dobro}")
print(f"O triplo de seu numero é: {numero_triplo}")
print(f"A raiz quadrada de seu numero é: {numero_raiz_quadrada:.2f}")