# faça um programa que leia um numero qualquer e mostre o seu fatorial. Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120

num = int(input("Digite um numero para calcular seu fatorial: "))

fatorial = 1

while num > 0:
    fatorial = fatorial * num 
    print(f"{num} x ", end="")
    num -= 1

print(f"= {fatorial}")