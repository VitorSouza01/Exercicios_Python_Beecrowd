"""
Leia um valor inteiro X (1 <= X <= 1000). Em seguida mostre os ímpares de 1 até X, um valor por linha, inclusive o X,
se for o caso.
"""

x = int(input())

if 1 <= x <= 1000:

    for n in range(1, x+2, 2):
        print(n)
