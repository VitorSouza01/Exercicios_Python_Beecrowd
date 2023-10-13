"""
Neste problema você deve ler um número que indica uma coluna de uma matriz na qual uma operação deve ser realizada, um
caractere maiúsculo, indicando a operação que será realizada, e todos os elementos de uma matriz M[12][12]. Em seguida,
calcule e mostre a soma ou a média dos elementos que estão na área verde da matriz, conforme for o caso. A imagem
abaixo ilustra o caso da entrada do valor 5 para a coluna da matriz, demonstrando os elementos que deverão ser
considerados na operação.
"""

coluna = int(input())

operacao = input().strip()

soma = 0

for i in range(12):

    for j in range(12):
        valor = float(input())

        if j == coluna:
            soma += valor

if operacao == "M":
    media = soma / 12
    resultado = media

elif operacao == "S":
    resultado = soma

print("%.1f" % resultado)
