# Faça um programa que leia um numero inteiro e mostre na tela o seu sucessor e seu antecessor.

numero = int(input("Digite um numero inteiro:\n"))
antecessor = numero - 1
sucessor = numero + 1

print(f"O seu numero é {numero} \nSeu antecessor é: {antecessor} \nSeu sucessor é: {sucessor}")