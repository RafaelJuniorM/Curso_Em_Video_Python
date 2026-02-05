# faça um progrma que leia tres numero e mostre qual é o MAIOR e qual é o MENOR.

numero1 = int(input("Digite o primeiro numero: "))
numero2 = int(input("Digite o segundo numero: "))
numero3 = int(input("Digite o terceiro numero: "))

menor = numero1
if numero2 < numero1 and numero2 < numero3:
    menor = numero2
if numero3 < numero1 and numero3 < numero2:
    menor = numero3

maior = numero1
if numero2 > numero1 and numero2 > numero3:
    maior = numero2
if numero3 > numero1 and numero3 > numero2:
    maior = numero3

print(f"O menor numero digitado foi {menor}")
print(f"O maior numero digitado foi {maior}")