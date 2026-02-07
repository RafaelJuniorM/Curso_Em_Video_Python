# escreva um progrma que leia um numero inteiro qualquer e peça para para o usuario escolher qual será a base de conversão:
# 1 para binário, 2 para octal e 3 para hexadecimal.

numero = int(input("DIgite o valor inteiro que deseja converter: "))
print("""Escolha a base de conversão:
    [1] Binario
    [2] Octal
    [3] Hexadecimal""")

opcao = int(input("Sua opção:  \n"))

if opcao == 1:
    print("="*30)
    print(" Você escolheu converter para Binário.")
    num_bin = bin(numero)
    print(f" O valor {numero} em Binario é  {num_bin}")
    print("="*30)
elif opcao == 2:
    print("="*30)
    print(" Voce escolheu converter para Octal.")
    num_oct = oct(numero)
    print(f" O valor {numero} em Octal é {num_oct}")
    print("="*30)
elif opcao == 3:
    print("="*30)
    print(" Voce escolheu converter para Hexadecimal.")
    num_hex = hex(numero)
    print(f" O valor {numero} em Hexadecimal é {num_hex}")
    print("="*30)
else: 
    print(" Opção inválida. Tente novamente.")