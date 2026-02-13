# exibi a tabuada de um numero que o usuario escolher, mostrando o resultado de 1 a 10.
print('==== Tabuada ====')
numero = int(input('Digite o numero que deseja ver a tabuada: '))

for tabuada in range(1, 11):
    resultado = numero * tabuada 
    print(f'{numero} X {tabuada} = {resultado}')