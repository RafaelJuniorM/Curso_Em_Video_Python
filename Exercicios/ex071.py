# crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. 
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.

produtos = (
    'Lapis', 1.50,
    'Caneta', 2.00,
    'Caderno', 15.00,
    'Borracha', 0.50,
    'Mochila', 120.00,
    'Estojo', 25.00,
    'Régua', 3.00,
    'Apontador', 1.00
)

print("-"*40)
print("LISTAGEM DE PREÇOS".center(40))
print("-"*40)

for element in range(0, len(produtos)):
    if element % 2 == 0:
        print(f"{produtos[element]:.<30}", end="")
    else: 
        print(f"R$ {produtos[element]:>7.2f}")
