# ESCREVA UM PROGRAMA QUE LEIA A VELOCIADDE DE UM CARRO. SE ELE ULTRAPASSAR 80KM/H, MOSTRE UMA MENSAGEM DIZENDO QUE ELE FOI MULTADO.
# A MULTA VAI CUSTAR R$7,00 POR CADA KM ACIMA DO LIMITE.

velocidade = int((input("Digite a sua velocidade em KM/h: ")))

if velocidade > 80:
    multa  = (velocidade - 80) * 7
    print(f"voce foi  multado!!! Sua multa será no valor de R${multa:.2f}")
else:
    print("Tenha um bom dia! Dirija com segurança!")