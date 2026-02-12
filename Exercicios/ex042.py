from random import choice

jogador = int(input('''Escolha uma opção:
[0] Pedra
[1] Papel
[2] Tesoura  

sua escolha:                                      
'''))

if jogador < 0 or jogador > 2:
    print("Opção inválida. Por favor, escolha um número entre 0 e 2.")
    exit()

itens = ('pedra', 'papel', 'tesoura')
escolha_maquina = choice(itens)

print(f'Você escolheu:   {itens[jogador]}')
print(f'A máquina escolheu:   {escolha_maquina}')

print("-=" * 11)

if jogador == 0: #pedra
    if escolha_maquina == "papel": 
        print("A Maquina ganhou!!")
    elif escolha_maquina =="tesoura":
        print("Você ganhou!!")
    else:
        print("Empate!!")

elif jogador == 1: # papel 
    if escolha_maquina == "tesoura":
        print("A Maquina ganhou!!")
    elif escolha_maquina == "pedra":
        print("Você ganhou!!")
    else:
        print("Empate!!")

elif jogador == 2: # tesoura
    if escolha_maquina == "papel":
        print("Você ganahou!!")
    elif escolha_maquina == "pedra":
        print("A Maquina ganhou!!")
    else:
        print("Empate!!")


