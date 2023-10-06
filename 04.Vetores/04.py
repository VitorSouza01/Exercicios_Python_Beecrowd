"""
Faça um programa que leia um vetor N[20]. Troque a seguir, o primeiro elemento com o último, o segundo elemento com o
penúltimo, etc., até trocar o 10º com o 11º. Mostre o vetor modificado.
"""

lista = []

for n in range(20):
    valor = int(input())
    lista.append(valor)

lista.reverse()
for m in range(20):
    print("N[%i] =" % m, lista[m])
