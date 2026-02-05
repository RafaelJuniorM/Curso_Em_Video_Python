# ESCREVA UM PROGRAMA QUE FAÇA O COMPUTADOR "PENSAR" EM UM NÚMERO INTEIRO ENTRE 0 E 5 E 
# PEÇA PARA O USUÁRIO TENTAR DESCOBRIR QUAL FOI O NÚMERO ESCOLHIDO PELO COMPUTADOR.
# O PROGRAMA DEVERÁ INFORMAR SE O USUÁRIO VENCEU OU PERDEU.

from random import randrange 
numero_sorteado = randrange(0,6)
numero_usuario = int(input("Escolha um numero entre 0 e 5:"))

print(f"O numero sorteado foi {numero_sorteado}")
if numero_sorteado == numero_usuario:
    print("PARABEEEEENS!!!!! VOCE ACERTOU O NUMERO")
else:
    print("QUE PENA, VOCE ERROU O NUMERO")

