# Crie um programa que leia a idade e o sexo de varias pessoas. A cada pessoa cadastrada,
#  o programa devera perguntar se o usuario quer ou nao continuar. No final, mostre:
# A) Quantas pessoas tem mais de 18 anos.
# B) Quantos homens foram cadastrados.
# C) Quantas mulheres tem menos de 20 anos.
from time import sleep


maior_idade = qtd_homens = qtd_mulheres_menos_20anos = 0 

print("-="*30)
print(" "*17+"CADASTRO DE PESSOA")
print("-="*30)

while True:
    idade = int(input("Idade: "))
    sexo = ' '

    while sexo not in "MF":
        print("Sexo invalido, tente novamente!")
        sexo = str(input(("Digite o sexo da pessoa [M/F]: "))).strip().upper()[0]
    
    if idade >= 18: 
        maior_idade += 1

    if sexo == "F" and idade < 20:
        qtd_mulheres_menos_20anos += 1
        
    if sexo == "M":
        qtd_homens += 1

    sleep(1)
    print("-="*30)
    print("CADASTRANDO ...")
    sleep(1)
    print("~"*30)
    print("Pessoa cadastrada com sucesso!!!")
    print("~"*30)

    deseja_continuar = ' '

    while deseja_continuar not in "SN":
        print("Resposta invalida, tente novamente!")
        deseja_continuar = str(input("Deseja continuar cadastrando pessoas? [S/N]: ")).strip().upper()[0]

    if deseja_continuar == "N":
        print("-="*30)
        print("Cadastro encerrado, volte sempre!")
        break

print("-="*30)
print(f"Quantidade de pessoas com mais de 18 anos: {maior_idade}")
print(f"Quantidade de homens cadastrados: {qtd_homens}")
print(f"Quantidade de mulheres com menos de 20 anos: {qtd_mulheres_menos_20anos}")
