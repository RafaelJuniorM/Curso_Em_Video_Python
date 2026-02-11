# Desenvolva uma logica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, 
# de acordo com a tabela abaixo:
# - Abaixo de 18.5: Abaixo do peso
# - Entre 18.5 e 25: Peso ideal
# - 25 até 30: Sobrepeso
# - 30 até 40: Obesidade
# - Acima de 40: Obesidade mórbida

peso = float(input("Digite o seu peso (kg): "))
altura = float(input("Digite sua altura (metro): "))

IMC = peso / (altura ** 2)
print(f"Seu IMC é de {IMC:.2f}")
if IMC <  18.5:
    print("Voce se encontra abaixo do peso")

elif IMC < 25:
    print("Voce se encontra no peso ideal") 

elif IMC < 30:
    print("Voce se encontra com sobrepeso")  
    
elif IMC <  40:
    print("Voce se encontra com obesidade")

elif IMC > 40:
    print("Voce se encontra com obesidade morbida")