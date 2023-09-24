"""
Faça um programa que leia 5 valores inteiros. Conte quantos destes valores digitados são pares e mostre esta informação.
"""

lista = []
valores_pares = 0

for n in range(5):
    valor = float(input())

    if valor % 2 == 0:
        lista.insert(0, valor)
        valores_pares = valores_pares + 1

print("%.i valores pares" % valores_pares)
