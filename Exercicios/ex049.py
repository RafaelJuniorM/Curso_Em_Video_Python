# Faça um programa que leia um numero inteiro e diga se ele é ou não um numero primo. 

numero = int(input("Digite um numero inteiro: "))
total = 0
for contador in range(1, numero+1):
    if numero % contador == 0:
        print("\033[33m", end="")
        total += 1
    else:
         print("\033[31m", end="")
    print(f"{contador}", end=" ")

print(f" \n\033[mO numero {numero} foi divisivel somente {total} vezes")
if total == 2:
    print(f"Portanto ele é PRIMO")