"""
Escreva um algoritmo que leia um inteiro N (0 ≤ N ≤ 100), correspondente a ordem de uma matriz M de inteiros, e
construa a matriz de acordo com o exemplo abaixo.
"""

while True:

    n = int(input())
    matriz = []
    linha = []

    if 0 <= n <= 100:

        if n > 1:

            # Matriz com Valor Inicial
            for i in range(1, n+1):
                linha.append(i)
                matriz.append(linha)

            # Matriz com Valor Roleta
            matriz_roleta = matriz[0][1:]

            for a in range(len(matriz_roleta)):
                matriz[1].insert(0, matriz_roleta[a])

            print(str(matriz[1][n-1:]).replace(",", "  ").replace("[", "  ").replace("]", ""))
            for b in range(1, len(matriz_roleta)+1):
                print(str(matriz[1][n-(b+1):-b]).replace(",", "  ").replace("[", "  ").replace("]", ""))

        elif n == 1:
            print("  1")

        elif n == 0:
            break

        print("")
