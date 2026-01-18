# faça um algoritmo que leia o o salario de um funcionário e mostre seu novo salário, com 15% de aumento.
salario_funcionario = float(input("Digite o salário do funcionário: R$  "))

aumento = 15/100 

novo_salario = salario_funcionario + (salario_funcionario * aumento)

print(f"O novo salário do funcionário é R$ {novo_salario:.2f}")