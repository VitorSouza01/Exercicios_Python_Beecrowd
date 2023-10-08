"""
Faça um programa que leia um valor N. Este N será o tamanho de um vetor X[N]. A seguir, leia cada um dos valores de X,
encontre o menor elemento deste vetor e a sua posição dentro do vetor, mostrando esta informação.
"""

n = int(input())
x = []

if 1 < n < 1000:
    x = input().split()

if len(x) == n:
    print("Menor valor: %s" % min(x))
    print("Posicao: %i" % x.index(min(x)))
