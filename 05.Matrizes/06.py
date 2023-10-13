"""
Leia um caractere maiúsculo, que indica uma operação que deve ser realizada e uma matriz M[12][12]. Em seguida, calcule
e mostre a soma ou a média considerando somente aqueles elementos que estão abaixo da diagonal Secundária da matriz,
conforme ilustrado abaixo (área verde).
"""

operacao = input().strip()

soma = 0
loop = 0

for i in range(12):

    for j in range(12):
        valor = float(input())

        if i + j > 11:
            soma += valor
            loop += 1

if operacao == "S":
    resultado = soma

elif operacao == "M":
    resultado = soma / loop

print("%.1f" % resultado)
