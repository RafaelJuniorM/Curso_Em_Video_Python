# Escreva um programa que pergunte o salario do funcionario e calcule o valor do seu aumento.
# Para salarios superiores a R$1250,00, calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%.    

salario = float(input("Digite o valor do salario: R$ "))

if salario <= 1250:
    novo_salario = salario + (salario * (15/100))
    print(f"O novo salario com aumento de 15% é R$ {novo_salario:.2f}")
else:
    novo_salario = salario + (salario * (10/100))
    print(f"O novo salario com aumento de 10% é R$ {novo_salario:.2f}")