# Faça um jogo onde o computador vai pensar em um numero entre 0 e 10. 
# O jogador vai tentar adivinhar qual foi o numero escolhido ate acertar, mostrando no final quantos palpites foram necessarios para vencer.

from random import randint 
num_tentativas = 0 
num_aleatorio = randint(0,10)
num_jogador = int(input('Tente adivinhar o numero que o computador pensou entre 0 e 10 \n Qual o seu palpite?  '))

while num_jogador != num_aleatorio:
    print("Numero errado, tente novamente. ")
    num_jogador = int(input('Tente adivinhar o numero que o computador pensou entre 0 e 10: '))
    num_tentativas += 1

print(f"**** Parabens, VOCE ACERTOU!! ***** \n voce precisou de {num_tentativas} tentativas.  ")
