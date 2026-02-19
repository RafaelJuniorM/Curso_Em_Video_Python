# Leia o primeiro termo e a razao de uma PA, mostrando os 10 primeiros termos da progressao. 
# Pergunte ao usuario se ele quer mostrar mais termos. O programa encerra quando ele disser que quer mostrar 0 termos.
# formula para calcular qualquer termo = An = A1 + (n-1)r  => onde n é o termo desejado. 

primeiro_termo = int(input('Digite o primeiro termo da PA: '))
razao  = int(input('Digite a razao da PA: '))
termo = primeiro_termo
cont = 1 
total_termos = 0
deseja_continuar = 10


print('-='*30)
while deseja_continuar != 0:
    total_termos += deseja_continuar
    while cont <= total_termos:
        print(f'{termo}',end=' -> ')
        termo += razao
        cont += 1

    
    deseja_continuar = int(input('Quantos termos voce deseja mostrar a mais? (Digite 0 para encerrar): '))
print('Finalizado')
print('-='*30)

