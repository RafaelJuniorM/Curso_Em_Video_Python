# Faça um programa que calcule a soma entre todos o numeros impares que 
# são multiplos de tres e que se encontram no intervalo entre 1 e 500.

soma = 0 
for num_impar in range(1, 501):
    if num_impar % 2 != 0 and num_impar % 3 == 0:
        soma += num_impar
        print(num_impar, end=' ')
print(f'\nA soma de todos os numeros impares multiplos de tres entre 1 e 500 é {soma}.')