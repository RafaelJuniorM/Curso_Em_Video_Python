# Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros.
print("==== conversor de metros para centimetros e milimetros ==== ")

valor_metros = float(input("Digite o valor em metros: "))

valor_centimetros = valor_metros*100
valor_milimetros = valor_metros*1000

print(f"O valor em metros é: {valor_metros:.2f}")
print(f"O valor em centimetros é: {valor_centimetros}")
print(f"O valor em milimetros é: {valor_milimetros}")

