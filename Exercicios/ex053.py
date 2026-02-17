# Faça um programa que leia o sexo de uma pessoa, mas so aceite os valores 'M' ou 'F'. 
# Caso esteja errado, peça a digitação novamente até ter um valor correto.

print('----- VERIFICADOR DE SEXO -----')

sexo = str(input('Digite o sexo [M/F]: ')).strip().upper()
while sexo not in 'MF': 
    print('Valor invalido, tente novamente.')
    sexo = str(input('Digite o sexo [M/F]: ')).strip().upper()
print('Sexo registrado com sucesso!')