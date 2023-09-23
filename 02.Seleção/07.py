"""
Leia 3 valores inteiros e ordene-os em ordem crescente. No final, mostre os valores em ordem crescente, uma linha em
branco e em seguida, os valores na sequência como foram lidos.

"""

valores = input().split()

for x in range(3):
    valores[x] = int(valores[x])

valores_original = valores.copy()

valores.sort()

# Ordem crescente
for y in range(3):
    print(valores[y])
print("")

# Ordem original
for z in range(3):
    print(valores_original[z])
