"""
Faça um programa que leia um vetor A[100]. No final, mostre todas as posições do vetor que armazenam um valor menor ou
igual a 10 e o valor armazenado em cada uma das posições.
"""

for n in range(100):
    valor = float(input())

    if valor <= 10:
        print("A[%i] =" % n, valor)
