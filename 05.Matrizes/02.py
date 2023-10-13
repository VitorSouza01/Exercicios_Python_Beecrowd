"""
Neste problema você deve ler um número, indicando uma linha da matriz na qual uma operação deve ser realizada, um
caractere maiúsculo, indicando a operação que será realizada, e todos os elementos de uma matriz M[12][12]. Em seguida,
calcule e mostre a soma ou a média dos elementos que estão na área verde da matriz, conforme for o caso. A imagem
abaixo ilustra o caso da entrada do valor 2 para a linha da matriz, demonstrando os elementos que deverão ser
considerados na operação.
"""

linha = int(input())

operacao = input().strip()

soma = 0

for i in range(12):

    for j in range(12):
        valor = float(input())

        if i == linha:
            soma += valor

if operacao == "S":
    resultado = soma

elif operacao == "M":
    media = soma / 12
    resultado = media

print("%.1f" % resultado)
