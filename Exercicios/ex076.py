# Crie um programa que vai ler vários numeros e colcoar em uma lista. Depois disso, mostre:
# A) Quantos numeros foram digitados
# B) A lista de valores, ordenada de forma decrescente
# C) Se o valor 5 foi digitado e está ou não na lista
lista = []
continuar = "Ss"

while True:
    num = int(input("Digite um valor: "))
    lista.append(num)

    continuar = str(input("Quer continuar? [S/N]")).strip().upper()[0]
    if continuar == "N":
        break
    qtd_num = len(lista)
    lista_ordenada = sorted(lista, reverse=True)

    if 5 in lista: 
        print("O valor 5 está presente na lista.")

print("Finalizando o programa...")
print("=-"*30)
print(f"Você digitou { qtd_num} números.")
print(f"A lista ordenada em descerente é:  { lista_ordenada}")
