# Crie um programa que mostre na tela todos os numeros pares 
# que esta no intervalo entre 1 e 50.
print ('==== todos os numeros pares entre 1 e 50 ====')

for num_pares in range(1, 51):
    if num_pares % 2 == 0:
        print(num_pares, end=' ')