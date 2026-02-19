# Crie um programa que leia varios numeros inteiros pelo teclado. no final da execução, 
# mostre a media entre todos os valores e qual foi o maior e o menor valores lidos. 
# O programa deve perguntar ao usuario se ele quer ou nçao continuar a digitar valores.



soma = 0
contador = 0 
media = 0 
continuar = "Ss"
maior = menor = 0 
while continuar in "Ss": 
    numero = int(input("Digite um numero: "))
    soma += numero
    contador += 1
    
    if contador == 1:
        maior = menor = numero 
    else:
        if numero > maior:
            maior = numero 
        if numero < menor:
            menor = numero
    continuar = str(input("Deseja continuar? [S/N]: ")).strip().upper()[0]

media = soma / contador
print(f"voce digitou {contador} numeros e a media dos numeros digitados é: {media:.2f}")
print(f"O maior valor digitado foi: {maior}")
print(f"O menor valor digitado foi: {menor}")
print("fim")