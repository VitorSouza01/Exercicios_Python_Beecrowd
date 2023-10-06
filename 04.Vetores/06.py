"""
Faça um programa que leia um valor T e preencha um vetor N[1000] com a sequência de valores de 0 até T-1 repetidas
vezes, conforme exemplo abaixo. Imprima o vetor N.
"""

lista_x = []
lista_y = []

t = int(input())

if 2 <= t <= 50:

    for n in range(1000):
        lista_x.append(n)

        for m in range(t):
            lista_y.append(m)

for o in range(1000):
    print("N[%i] =" % lista_x[o], lista_y[o])
