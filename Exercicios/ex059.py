# crie um programa que leia varios numeros inteiros pelo teclado. 
# O programa so vai parar quando o usuario digitar o valor 999, que e a condicao de parada. 
# No final, mostre quantos numeros foram digitados e qual foi a soma entre eles (desconsiderando o flag).

num = int(input("Digite um numero inteiro [999 para parar]: "))

soma = 0
contador = 0

while num!= 999:
    soma += num
    num = int(input("Digite um numero inteiro [999 para parar]: "))
    contador += 1

print(f'Voce digitou {contador} numeros e a soma entre eles foi {soma}.')