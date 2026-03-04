# Crie um programa que tenha uma tupla com os 20 primeiros colocados da tabela do Campeonato Brasileiro de Futebol,
# na ordem de colocação. Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Uma lista com os times em ordem alfabética.
# d) Em que posição está o time da Chapecoense.

times = ("Palmeiras" , "São Paulo" , "Corinthians", "Bahia", "Fluminense", "Athletico Paranaense", 
         "Red Bull Bragantino", "Grêmio", "Chapecoense", "Mirassol", "Flamengo", "Coritiba", "Botafogo", 
         "Vitória", "Remo", "Atlético-MG", "Internacional", "Cruzeiro", "Vasco da Gama", "Santos")

print("-="*30)
print(f"Os 5 primeiros colocados são: {times[0:5]}")
print("-="*30)
print(f"Os 4 ultimos colocados são: {times[-4:]}")
print("-="*30)
print(f"Os times em ordem alfabetica são: {sorted(times)}")
print("-="*30)
print(f"O time da Chapecoense esta na {times.index('Chapecoense')+1}ª posição")