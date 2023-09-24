"""
Leia um valor inteiro N. Este valor será a quantidade de valores que serão lidos em seguida. Para cada valor lido,
mostre uma mensagem em inglês dizendo se este valor lido é par (EVEN), ímpar (ODD), positivo (POSITIVE) ou negativo
(NEGATIVE). No caso do valor ser igual a zero (0), embora a descrição correta seja (EVEN NULL), pois por definição zero
é par, seu programa deverá imprimir apenas NULL.
"""

n = int(input())

for m in range(n):
    valores = int(input())

    if valores == 0:
        print("NULL")

    elif valores > 0:

        if valores % 2 == 0:
            print("EVEN POSITIVE")

        elif valores % 2 == 1:
            print("ODD POSITIVE")

    elif valores < 0:

        if valores % 2 == 0:
            print("EVEN NEGATIVE")

        elif valores % 2 == 1:
            print("ODD NEGATIVE")
