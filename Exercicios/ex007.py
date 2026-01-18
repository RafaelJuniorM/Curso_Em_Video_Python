# Desenvolva um programa que leia duas notas de uma aluno, calcule e mostre sua media. 

nota_um = float(input("Digite a primeira nota: "))
nota_dois =  float(input("Digite a segunda nota:  "))

media_notas = (nota_um + nota_dois) / 2 

print(f" A primeira nota é: {nota_um} \n A segunda nota é: {nota_dois} \n A media das notas é: {media_notas:.2f}")