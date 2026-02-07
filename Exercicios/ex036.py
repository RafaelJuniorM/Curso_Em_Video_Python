# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade:
# - Se ele ainda vai se alistar ao serviço militar.
# - Se é a hora de se alistar.
# - Se já passou do tempo de alistamento.
import datetime

nascimento = int(input("Digite o ano de nascimento: "))
ano_atual = datetime.datetime.now().year
idade = ano_atual - nascimento

if idade < 18:
    print(f"\nVoce nasceu em {nascimento} tem {idade} anos em {ano_atual} e ainda vai se alistar ao serviço militar.")
    print(f"Ainda faltam {18 - idade} anos para o alistamento.")
    print(f"Seu alistamento será em {nascimento + 18} \n")

elif idade > 18:
    print(f"\nVoce nasceu em {nascimento} tem {idade} anos em {ano_atual} e já passou do tempo de se alistar ao serviço militar.")
    print(f"Passaram-se {idade - 18} anos desde o alistamento.")
    print(f"Seu alistamento foi em {nascimento + 18} \n")

elif idade == 18:
    print(f"\nVoce nasceu em {nascimento} tem {idade} anos em {ano_atual} e é a hora de se alistar ao serviço militar.")
    print(f"Seu alistamento é este ano, {ano_atual} \n")
