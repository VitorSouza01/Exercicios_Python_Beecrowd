"""
Leia 3 valores de ponto flutuante e efetue o cálculo das raízes da equação de Bhaskara. Se não for possível calcular as
 raízes, mostre a mensagem correspondente “Impossivel calcular”, caso haja uma divisão por 0 ou raiz de numero negativo.
"""

valores = input().split()

valor_a = float(valores[0])
valor_b = float(valores[1])
valor_c = float(valores[2])

delta = (valor_b * valor_b) - 4 * (valor_a * valor_c)
raiz_delta = delta**(1/2)

if valor_a != 0:

    if delta > 0:
        x1 = (-(valor_b) + raiz_delta) / (2 * valor_a)
        x2 = (-(valor_b) - raiz_delta) / (2 * valor_a)

        if x1 or x2 != 0:
            print("R1 = %.5f" % x1)
            print("R2 = %.5f" % x2)

        else:
            print("Impossivel calcular")

    else:
        print("Impossivel calcular")

else:
    print("Impossivel calcular")