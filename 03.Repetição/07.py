"""
Leia um valor inteiro X. Em seguida apresente os 6 valores ímpares consecutivos a partir de X, um valor por linha,
inclusive o X ser for o caso.
"""

x = int(input())
numeros_impares = 0

while numeros_impares < 6:

    if x % 2 != 0:
        print(x)
        numeros_impares += 1

    x += 1
