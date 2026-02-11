# confederação Nacional de natação precisa de um programa que leia o ano de nascimento 
# de um atleta e mostre sua categoria, de acordo com a idade:
# - até 9 anos: mirim
# - até 14 anos: infantil
# - até 19 anos: junior
# - até 25 anos: sênior
# - acima: master

from datetime import date 

ano = int(input("DIgite o ano de nascimento do atleta: "))
atual = date.today().year
idade = atual - ano

if idade <= 9:
    print(f"O atleta possui {idade} anos, sua categoria é MIRIM")
elif idade <= 14:
    print(f"O atleta possui {idade} anos, sua categoria é INFANTIL")
elif idade <= 19:
    print(f"O atleta possui {idade} anos, sua categoria é JUNIOR")
elif idade <= 25:
    print(f"O atleta possui {idade} anos, sua categoria é SÊNIOR")
elif idade > 25:
    print(f"O atleta possui {idade} anos, sua categoria é MASTER")