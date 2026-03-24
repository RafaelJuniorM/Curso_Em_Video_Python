# crie um programa onde o usuário possa digitar cinco valores numericos e cadastre-os
# em uma lista,
# já na posição correta de inserção (sem usar o sort()).
# No final, mostre a lista ordenada na tela.

valores = []

for contador in range(0, 5):
    num = int(input("Digite um valor: "))
    valores.append(num)
    print(contador)

print("=-"*30)
print(f"Os valores digitados foram {valores}")
   

   


