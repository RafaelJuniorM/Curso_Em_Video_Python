# Faça um programa que mostre a tabuada de varios numeros, um de cada vez, para cada valor digitado pelo usuario.
#  O programa sera interrompido quando o numero solicitado for negativo.
print("-="*30)
print(" "*27+"TABUADA")
print("-="*30)
while True:
    numero = int(input("Digite o numero que deseja ver a tabuada [Digite 0 para encerrar o programa]: "))
    if numero == 0 :
        print("-="*30)
        print("Programa encerrado, volte sempre!")
        print("-="*30)
        break
        
    for contador in range(1,11):
        resultado = numero * contador
        print(f"{numero} X {contador} = {resultado}" )
