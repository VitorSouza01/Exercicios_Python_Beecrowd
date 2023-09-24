"""
Leia 5 valores Inteiros. A seguir mostre quantos valores digitados foram pares, quantos valores digitados foram ímpares,
quantos valores digitados foram positivos e quantos valores digitados foram negativos.
"""

valores_pares = 0
valores_impares = 0
valores_positivos = 0
valores_negativos = 0

for n in range(5):
    valor = float(input())

    # Valores Pares
    if valor % 2 == 0:
        valores_pares += 1

    # Valores Impares
    elif valor % 2 == 1:
        valores_impares += 1

    # Valores Positivos
    if valor > 0:
        valores_positivos += 1

    # Valores Negativos
    elif valor < 0:
        valores_negativos += 1

print("%i valor(es) par(es)" % valores_pares)
print("%i valor(es) impar(es)" % valores_impares)
print("%i valor(es) positivo(s)" % valores_positivos)
print("%i valor(es) negativo(s)" % valores_negativos)
