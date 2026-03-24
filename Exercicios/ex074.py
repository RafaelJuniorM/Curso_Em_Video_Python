# Crie um programa onde o usuário possa digitar varios valores numericos e cadastre-os em uma lista.
# Caso o numero já exista lá dentro, ele não será adicionado.
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

valores = []
continuar  ="Ss"

while continuar in "Ss":
    valores.append(int(input("Digite um valor:")))
    print(f"Valor adicionado com sucesso...")
    if valores.count(valores[-1]) > 1:
        print("Valor já existente na lista, não será adicionado.")
        valores.pop()
    
    continuar = str(input("Deseja continuar? [S/N]  ")).strip().upper()[0]



print("=-"*30)
print(f"Você digitou os valores {sorted(valores)}")

# OUTRA MANEIRA DE FAZER ISSO:

numeros = []
while True: 
    n = int(input("Digite um valor: "))
    if n not in numeros:
        numeros.append(n)
        print("Valor adicionado com sucesso...")
    else:
        print(" Valor duplicado! Não vou adicionar...")
    r = str(input("Quer continuar? [S/N]")).strip().upper()[0]
    if r == "Nn":
        break

print("=-"*30)
numeros.sort()
print(f"Você digitou os valores {numeros}")