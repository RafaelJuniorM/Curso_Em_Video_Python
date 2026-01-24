# Faça um programa que leia um angulo qualquer e mostrre na tela o valor seno, cosseno e tangente desse angulo.
# 

import math

angulo = float(input("Informe o valor do angulo: "))

seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

print(f"Para o angulo de {angulo}" )
print(f"O valor do SENO: {seno:.2f}")
print(f"O valor do COSSENO: {cosseno:.2f}")
print(f"O valor da TANGENTE: {tangente:.2f}")