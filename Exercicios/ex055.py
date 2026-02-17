# Crie um progrma que leia dois valores e mostre um menu na tela:
# [1] somar
# [2] multiplicar
# [3] maior
# [4] novos numeros
# [5] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.

val_1 = int(input('Digite o primeiro valor: '))
val_2 = int(input('Digite o segundo valor:  '))

opcao = 0
while opcao !=5: 
    print('''----- MENU DE OPÇÕES -----
    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos numeros
    [5] sair do programa''')


    opcao = int(input('>>>>>>> Digite a opcao desejada: '))
    if opcao ==1:
        soma = val_1 + val_2
        print("="*30)
        print("Voce escolheu somar os dois valores")
        print(f"A soma entre {val_1} + {val_2} é igual a {soma}")
        print("="*30)
    elif opcao == 2:
        multiplica = val_1 * val_2
        print("="*30)
        print("Voce escolheu multiplicar os dois valores")
        print(f"A multiplicacao entre {val_1} x {val_2} é igual a {multiplica}")
        print("="*30)
    elif opcao == 3:
        print("="*30)
        print("Voce escolheu mostrar o maior valor entre os dois")

        if val_1 > val_2:
            print(f"O maior valor é {val_1}")
        elif val_2 > val_1:    
             print(f"O maior valor é {val_2}")
        else:
            print("Os dois valores são iguais")
        print("="*30)
    elif opcao == 4:
        print("="*30)
        print("Voce escolheu digitar novos numeros")
        val_1 = int(input('Digite o primeiro valor: '))
        val_2 = int(input('Digite o segundo valor:  '))
        print("="*30)
    elif opcao == 5:
        print("="*30)
        print("Voce escolheu sair do programa, até mais!")
        print("="*30)