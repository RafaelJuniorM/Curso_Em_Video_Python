# Crie um programa que vai ler varios números e colocar em uma lista. 
# Depois disso, crie duas lista extras que vao conter apenas os valores pares e os valores impares digitados, 
# respectivamente.
# Ao final, mostre o conteudo das tres listas geradas.

lista = []
par = []
impar = []
while True:
    numero = int(input("Digite um valor: "))
    lista.append(numero)

    if numero% 2 == 0:
        par.append(numero)
    else:
        impar.append(numero)

    continuar = str(input("Deseja continuar? [S/N]")).strip().upper()[0]
    if continuar in "N":
        break
            
                
print("Finalizando o programa...")
print("=-"*30)

print(f"A lista completa é: {lista}")
print(f"A lista de pares é: {par}")
print(f"A lista de impares é: {impar}")
