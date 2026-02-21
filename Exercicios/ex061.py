# Crie um programa que leia varios numeros inteiro pelo teclado. O programa só vai parar quando o usuario digitar o valor 999, 
# que é a condição de parada. No final, mostre quantos numeros foram digitados e qual foi a soma entre eles (desconsiderando o flag).
soma = contador = 0
while True:
    numero = int(input("Digite um numero inteiro [999 para encerrar o programa]: "))
    if numero == 999:
        break

    soma += numero
    contador += 1

print("-="*30)
print(f"voce digitou {contador} numeros e a soma entre eles foi de {soma}")