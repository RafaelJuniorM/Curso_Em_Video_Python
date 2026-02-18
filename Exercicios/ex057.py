# Leia o primeiro termo e a razao de uma PA, mostrando os 10 primeiros termos da progressao. 
# Pergunte ao usuario se ele quer mostrar mais termos. O programa encerra quando ele disser que quer mostrar 0 termos.
# formula para calcular qualquer termo = An = A1 + (n-1)r  => onde n é o termo desejado. 

primeiro_termo = int(input('Digite o primeiro termo da PA: '))
razao  = int(input('Digite a razao da PA: '))

termo = primeiro_termo
cont = 1 

deseja_continuar = 1

while cont <=10:
    print(f'{termo}',end=' -> ')
    termo += razao
    cont += 1

deseja_continuar = int(input(
     ' \n Deseja mostrar mais termos? Se sim, informe a quantidade caso NÃO tecle [0]: '))

while deseja_continuar != 0:
        while cont <= deseja_continuar:
            print(f'{termo}',end=' -> ')
            termo += razao
            cont += 1
      
print('Finalizado')



