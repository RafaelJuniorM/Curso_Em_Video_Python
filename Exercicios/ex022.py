# Crie um programa que leia o nome completo de um pessoa e mostre:
# - O nome com todas as letras maiúsculas e minúsculas.
# - Quantas letras ao todo (sem considerar espaços).
# - Quantas letras tem o primeiro nome.

nome_completo = input("Digite seu nome completo: ")

nome_maiusculo = nome_completo.upper()
nome_minusculo = nome_completo.lower()
quantidade_letras = len(nome_completo.replace(" ",""))
primeiro_nome = nome_completo.split()[0]

print("Nome em maiúsculas:", nome_maiusculo)
print("Nome em minúsculas:", nome_minusculo)
print("Quantidade de letras (sem espaços):", quantidade_letras)
print("Quantidade de letras no primeiro nome:", len(primeiro_nome))