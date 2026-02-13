# Desenvolva um programa que leia seis numero inteiro e mostre a soma 
# apenas daqueles que forem pares. 
# Se o valor digitado for impar, desconsidere-o.

soma_paares = 0 

for soma in range(1,7):
    numero = int(input('Digite um numero inteiro: '))
    if numero % 2 ==0:
        soma_paares += numero
print(f'A soma dos numeros pares é {soma_paares}')