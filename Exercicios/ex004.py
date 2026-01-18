# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e 
# todas as informações possíveis sobre ele.

# ler o dado pelo usuarrio 
dado = input("Digite algo:  \n")

# mostrar o tipo primitivo do dado
type_dado = type(dado)
print(f"O tipo primitivo desse valor é: {type_dado}")

# veririfica se e espaço
dado_espaco = dado.isspace()
print(f"É um espaço? {dado_espaco}")

# verifica se e numero 
number_dado = dado.isnumeric()
print(f"É um numero? {number_dado}")

# verifica se e alfabeto
dado_alfabetico = dado.isalpha()
print(f"É alfabetico? {dado_alfabetico}")

# verifica se e alfanumerico
dado_alfanumerico = dado.isalnum()
print(f"É alfanumerico? {dado_alfanumerico }")

# veririfica se e maiusculo
dado_maiusculo = dado.isupper()
print(f" Está em maiusculas? {dado_maiusculo}")

# verifica se esta em minuscula
dado_minuscula = dado.islower()
print(f"Esta em minusculas? {dado_minuscula}")

# verifica se esta capitalizada - nem maiscula nem minuscula, mas com a primeira letra maiuscula
dado_capitalizada = dado.istitle()
print(f"Está capitalizada? {dado_capitalizada}")