#operacao = input().strip()

soma = 0
loop = 0

for i in range(12):

    for j in range(12):
        valor = float(input())

        """
        if i < j:
            soma += valor
            loop += 1
            print(i, j)
        """
        while i <= 5 and j :
            soma += valor
            loop += 1
            print(i, j)

"""
if operacao == "S":
    resultado = soma

elif operacao == "M":
    resultado = soma / loop

print("%.1f" % resultado)
"""