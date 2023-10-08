"""
Faça um programa que leia um valor N. Este N será o tamanho de um vetor X[N]. A seguir, leia cada um dos valores de X,
encontre o menor elemento deste vetor e a sua posição dentro do vetor, mostrando esta informação.
"""

n = int(input())

x = list(map(int, input().split()))

menor_valor = x[0]
posicao = 0

for i in range(1, n):
    if x[i] < menor_valor:
        menor_valor = x[i]
        posicao = i

print("Menor valor: %s" % menor_valor)
print("Posicao: %i" % posicao)
