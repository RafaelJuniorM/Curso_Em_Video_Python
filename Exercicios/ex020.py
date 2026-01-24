import random


nome_primeiro_aluno = input("Informe o nome do primeiro aluno: ")
nome_segundo_aluno = input("Informe o nome do segundo aluno: ")
nome_terceiro_aluno = input("Informe o nome do terceiro aluno: ")
nome_quarto_aluno = input("Informe o nome do quarto aluno: ")

alunos =[ nome_primeiro_aluno, nome_segundo_aluno, nome_terceiro_aluno, nome_quarto_aluno]

random.shuffle(alunos)

print(f"A ordem de apresentação dos alunos será: {alunos}")