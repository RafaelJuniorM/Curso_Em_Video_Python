# Elabore um programa que calcule o valor a ser paga por um produto, 
# considerando o seu preço normal e condição de pagamento:
# - À vista dinheiro/cheque: 10% de desconto
# - À vista no cartão: 5% de desconto
# - Em até 2x no cartão: preço normal
# - 3x ou mais no cartão: 20% de juros

preco = float(input("Digite o preço das compras: R$ "))
print("=" * 5 + ' LOJAS RAFAEL ' + "=" * 5)
print("Formas de pagamento")
print("""
[1] À vista dinheiro/cheque
[2] À vista no cartão
[3] Em até 2x no cartão
[4] 3x ou mais no cartão

""")
opcao = int(input("Qual opção de pagamento? "))
if opcao == 1:
    print("Seu pagamento será a vista, com isso você tem direito a 10% de desconto")
    total = preco - (preco *10/100)
   

elif opcao == 2:
    print("Seu pagamento será a vista no cartão, com isso você tem direito a 5% de desconto")
    total = preco - (preco * 5/100)

elif opcao == 3:
    print("Seu pagamento será parcelado em até 2x no cartão, com isso você não terá desconto")
    total =  preco
    parcela = total / 2
    
elif opcao == 4:
    parcela = int(input("Quantas parcelas deseja dividir? "))
    print(f"Seu pagamento será parcelado em {parcela} ou mais no cartão, com isso você terá 20% de juros")
    total = preco + (preco * 20/100)
    total_parcela = total / parcela
    total_juros = total - preco
    print(f"Sua compra de R$ {preco:.2f} será parcelada em {parcela}x de R$ {total_parcela:.2f} com juros")
    print(f"O valor total dos juros é de R$ {total_juros:.2f}")

else :
    total = preco
    print("Opção de pagamento inválida, tente novamente")


print(f"SUa compra de R$ {preco:.2f} vai custar R$ {total:.2f} no final")