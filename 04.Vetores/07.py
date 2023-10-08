"""
Leia um valor X. Coloque este valor na primeira posição de um vetor N[100]. Em cada posição subsequente de N (1 até 99),
coloque a metade do valor armazenado na posição anterior, conforme o exemplo abaixo. Imprima o vetor N.
"""

lista = []

x = float(input())

for m in range(100):
    lista.append(x)
    x /= 2

for n in range(100):

    print("N[%i] =" % n, "%.4f" % lista[n])
