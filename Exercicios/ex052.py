# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final 
# do programa, mostre:
# a media da idade, o nome do homem mais velho e quantas mulhes tem menos de 20 anos. 


soma_idade = 0
Qtd_mulheres = 0
idade_homem_velho = 0
nome_homem_velho = ''
Qtd_mulheres = 0
media_idade = 0

for pessoas in range(1,3):
    print(f"----- {pessoas}ª PESSOA -----")
    nome = str(input('Digite o nome: ')).strip()
    idade = int(input('Digite a idade: '))
    sexo = str(input('Digite o sexo [M/F]: ')).strip().upper()


    soma_idade += idade 
    

    if sexo == 'F' and idade < 20:
        Qtd_mulheres += 1

    if sexo =='M':
        if pessoas == 1: 
            idade_homem_velho = idade
            nome_homem_velho = nome
        else: 
           if idade > idade_homem_velho:
                idade_homem_velho = idade
                nome_homem_velho = nome 

media_idade = soma_idade / 2


print(f"A media de idade do grupo é de {media_idade:.2f} anos")
print(f"O homem mais velho é {nome_homem_velho} com {idade_homem_velho} anos")
print(f"Quantidade de mulheres com menos de 20 anos: {Qtd_mulheres}")