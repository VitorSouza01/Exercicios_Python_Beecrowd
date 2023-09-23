"""
Leia 3 valores reais (A, B e C) e verifique se eles formam ou não um triângulo. Em caso positivo, calcule o perímetro
do triângulo e apresente a mensagem:

Perimetro = XX.X

Em caso negativo, calcule a área do trapézio que tem A e B como base e C como altura, mostrando a mensagem

Area = XX.X
"""

valores = input().split()

vlr_a = float(valores[0])
vlr_b = float(valores[1])
vlr_c = float(valores[2])

if (vlr_b - vlr_c) < vlr_a < (vlr_b + vlr_c):

    if (vlr_a - vlr_c) < vlr_b < (vlr_a + vlr_c):

        if (vlr_a - vlr_b) < vlr_c < (vlr_a + vlr_b):
            perimetro = vlr_a + vlr_b + vlr_c
            print("Perimetro = %.1f" % perimetro)

        else:
            trapezio = ((vlr_a + vlr_b) * vlr_c) / 2
            print("Area = %.1f" % trapezio)

    else:
        trapezio = ((vlr_a + vlr_b) * vlr_c) / 2
        print("Area = %.1f" % trapezio)

else:
    trapezio = ((vlr_a + vlr_b) * vlr_c) / 2
    print("Area = %.1f" % trapezio)
