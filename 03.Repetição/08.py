"""
Leia 2 valores inteiros X e Y. A seguir, calcule e mostre a soma dos números impares entre eles.
"""

x = int(input())
y = int(input())
lista = []

diferenca = x - y

for n in range(y+1, x):
    if n % 2 != 0:
        lista.append(n)

print(sum(lista))
