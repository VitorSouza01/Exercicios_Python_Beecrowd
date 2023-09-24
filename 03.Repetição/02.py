"""
Faça um programa que leia 6 valores. Estes valores serão somente negativos ou positivos (desconsidere os valores nulos).
A seguir, mostre a quantidade de valores positivos digitados.
"""

lista = []
valores_positivos = 0

for n in range(6):
    valor = float(input())

    if valor > 0:
        lista.insert(0, valor)
        valores_positivos = valores_positivos + 1

print("%.i valores positivos" % valores_positivos)
