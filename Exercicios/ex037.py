# Crie um programa que leia duas notas de um aluno e calcule sua media, mostrando uma mensagem no final, de acordo com a média atingida:
# - Média abaixo de 5.0: REPROVADO
# - Média entre 5.0 e 6.9: RECUPERAÇÃO
# - Média 7.0 ou superior: APROVADO
primeira_notqa = float(input("Digite a primeira nota: "))
segunda_nota = float(input("Digite a segunda nota: "))  

media_nota = (primeira_notqa + segunda_nota) /2

if media_nota < 5.0:
    print(f"\n Sua média é {media_nota:.1f} e você está REPROVADO \n")

elif media_nota >= 5.0 and media_nota <= 6.9:
    print(f"\n Sua média é {media_nota:.1f} e você está de RECUPERAÇÃO \n")

else:
    print(f"\n Sua média é {media_nota:.1f} e você está APROVADO \n")
