"""
Leia 6 valores. Em seguida, mostre quantos destes valores digitados foram positivos.
Na próxima linha, deve-se mostrar a média de todos os valores positivos digitados, com um dígito após o ponto decimal.
"""

lista = []
valores_positivos = 0

for n in range(6):
    valor = float(input())

    if valor > 0:
        lista.insert(0, valor)
        valores_positivos = valores_positivos + 1

media_valores = sum(lista) / len(lista)

print("%.i valores positivos" % valores_positivos)
print("%.1f" % media_valores)
