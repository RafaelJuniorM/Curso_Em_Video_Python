# Escreva um programa que leia um numero n inteiro qualquer e mostre na tela os N primeiro elementos de uma Sequencia de Fibonacci. 
# Ex: 0 - 1 - 1 - 2 - 3 - 5 - 8
#         t1+t2   t3
print('-='*30)
print('Sequencia de Fibonacci')
print('-='*30)

num = int(input("Quantos termos que mostrar da sequencia de Fibonacci: "))

termo1 = 0
termo2 = 1 
print(f'{termo1} -> {termo2} -> ', end='')
contador = 3
while contador < num:
    
    termo3 = termo1 + termo2
    print(f'{termo3} -> ', end='')
    
    termo1 = termo2
    termo2 = termo3
    contador += 1

print("Finalizado")
