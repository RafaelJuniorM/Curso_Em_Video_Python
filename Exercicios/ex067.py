# Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

cont_extenso = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove',
                'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True: 
        num = int(input('Digite um numero entre 0 e 20: '))
        if num > 20:
            print("Numero invalido, tente novamente!")
           
        else:
            print("-="*30)
            print(f"O numero digitdo por extenso é: {cont_extenso[num]}")
            print("-="*30)

 