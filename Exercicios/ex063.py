# Faça um programa que jogue par ou impar com o computador. 
# O jogo só sera interrompido quando o jogador perder, mostrando o total de vitorias consecutivas que ele conquistou no final do jogo.

from random import randint


vitorias_consecutivas = 0

print("-="*30)
print(" "*27+"JOGO PAR OU IMPAR")
print("-="*30)


while True:
    num_jogador = int(input("Digite um numero inteiro para o jogo: "))
    num_computador = randint(0,10)
    
    escolha_jogador = str(input("Par ou Impar? [P/I]:")).strip().upper()[0]
    if escolha_jogador == "P":
        escolha_computador = "I"
        print(" \n \n Voce escolheu PAR, o computador ficou com IMPAR")
    else:
        escolha_computador = "P"
        print(" \n \n Voce escolheu IMPAR, o computador ficou com PAR")

    
    soma = num_jogador + num_computador
    par_ou_impar = soma % 2

    if par_ou_impar == 0:
        resultado = "P"
        if escolha_jogador == resultado:
            print("-="*30)
            print(f"Voce jogou {num_jogador} e o computador jogou {num_computador}.")
            print(f"Soma dos numero deu {soma}, sendo PAR")
            print("~"*30)
            print("PARABENS!!! VOCE VENCEU!!!")
            print("-="*30)
            vitorias_consecutivas += 1

        else:
            print("-="*30)
            print(f"Voce jogou {num_jogador} e o computador jogou {num_computador}.")
            print(f"Soma dos numero deu {soma}, sendo PAR")
            print("~"*30)
            print("QUE PENA!!! VOCE PERDEU!!!")
            print("-="*30)
            break
        
    else:
        resultado = "I"
        if escolha_jogador == resultado:
            print("-="*30)
            print(f"Voce jogou {num_jogador} e o computador jogou {num_computador}.")
            print(f"Soma dos numero deu {soma}, sendo IMPAR")
            print("~"*30)
            print("PARABENS!!! VOCE VENCEU!!!")
            print("-="*30)

          
            vitorias_consecutivas += 1
        else:
            print("-="*30)
            print(f"Voce jogou {num_jogador} e o computador jogou {num_computador}.")
            print(f"Soma dos numero deu {soma}, sendo IMPAR")
            print("~"*30)
            print("QUE PENA!!! VOCE PERDEU!!!")
            print("-="*30)
            break
    print(" "*10+"A MAQUINA QUER UMA REVANCHE!!!  VAMOS NOVAMENTE!!!")
    print("-="*30)

if vitorias_consecutivas == 0:
    print("Voce nao venceu nenhuma vez, tente novamente!")
else:
    print(f"Voce venceu {vitorias_consecutivas} vezes consecutivas")