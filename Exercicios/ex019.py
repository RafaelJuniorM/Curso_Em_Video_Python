# Um professor quer sortear um dos seua quatro alunos para apagar o quadro. 
# Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.

import random


nome_primeiro_aluno = input("Informe o nome do primeiro aluno: ")
nome_segundo_aluno = input("Informe o nome do segundo aluno: ")
nome_terceiro_aluno = input("Informe o nome do terceiro aluno: ")
nome_quarto_aluno = input("Informe o nome do quarto aluno: ")

alunos =[ nome_primeiro_aluno, nome_segundo_aluno, nome_terceiro_aluno, nome_quarto_aluno]

aluno_sorteado = random.choice(alunos)

print(f" O aluno escolhido foi: {aluno_sorteado}")