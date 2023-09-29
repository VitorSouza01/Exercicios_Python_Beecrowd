"""
Faça um programa que leia um vetor X[10]. Substitua a seguir, todos os valores nulos e negativos do vetor X por 1. Em
seguida mostre o vetor X.
"""

vetor = []

for n in range(10):
    valor = int(input())
    vetor.append(valor)

    if vetor[n] == 0:
        vetor[n] = 1
        print("X[%i] =" % n, vetor[n])

    elif vetor[n] < 0:
        vetor[n] = 1
        print("X[%i] =" % n, vetor[n])

    else:
        print("X[%i] =" % n, vetor[n])
