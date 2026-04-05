# Crie um programa que vai ler vários numeros e colcoar em uma lista. Depois disso, mostre:
# A) Quantos numeros foram digitados
# B) A lista de valores, ordenada de forma decrescente
# C) Se o valor 5 foi digitado e está ou não na lista
lista = []
continuar = "Ss"

while True:
    lista.append(int(input("Digite um valor: ")))

    continuar = str(input("Quer continuar? [S/N]")).strip().upper()[0]
    if continuar in "Nn":
        break
   

print("Finalizando o programa...")

print("=-"*30)

qtd_num = len(lista)
lista_ordenada = sorted(lista, reverse=True)

print(f"Você digitou {qtd_num} números.")
print(f"A lista ordenada em descerente é:  { lista_ordenada}")
if 5 in lista: 
        print("O valor 5 está presente na lista.")
else:
        print("O valor 5 não está presente na lista.")
