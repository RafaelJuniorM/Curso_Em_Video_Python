# crie um programa que simule o funcionamento de um caixa eletronico. 
# No inicio, pergunte ao usuario qual sera o valor a ser sacado (numero inteiro) 
# e o programa vai informar quantas cedulas de cada valor serao entregues.
# OBS: Considere que o caixa eletronico possui cedulas de R$50, R$20, R$10 e R$1.

print("="*30)
print(" "*7+"CAIXA ELETRONICO")
print("="*30)

valor_saque = int(input("Informe o valor a ser sacado: R$ "))
valor_total = valor_saque
valor_cedula = 50 
total_cedula = 0
while True: 
    if valor_total >= valor_cedula:
        valor_total -= valor_cedula
        total_cedula += 1

    else:
        if total_cedula > 0:
            print(f"Total de {total_cedula} cedulas de R$ {valor_cedula}")
        if valor_cedula == 50:
            valor_cedula = 20
        elif valor_cedula == 20:
            valor_cedula = 10
        elif valor_cedula == 10:
            valor_cedula = 1
        if valor_total == 0:
            break
