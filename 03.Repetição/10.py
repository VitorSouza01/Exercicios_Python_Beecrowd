"""
Leia um valor inteiro N. Apresente o quadrado de cada um dos valores pares, de 1 até N, inclusive N, se for o caso.
"""

n = int(input())

if 5 < n < 2000:

    for m in range(1, n+1):

        if m % 2 == 0:
            quadrado = m ** 2
            print("%i^2" % m, end=""), print(" = %i" % quadrado)
