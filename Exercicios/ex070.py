# Desenvolva um programaa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# a) Quantas vezes apareceu o valor 9.
# b) Em que posição foi digitado o primeiro valor 3.
# c) Quais foram os números pares.

numero = ((int(input('Digite um numero:'))), (int(input('Digite um numero:'))),(int(input('Digite um numero:'))),(int(input('Digite um numero:'))))

print(f'Os números digitados foram: {numero}')
print(f"O numero 9 apareceu {numero.count(9)} vezes")

if 3 in numero:
    print(f"o numero 3 apareceu na posição {numero.index(3)}")

for elements in numero:
    if elements % 2 == 0:
        print(f'Os números pares foram: {elements}')

