"""
Leia 2 valores com uma casa decimal (x e y), que devem representar as coordenadas de um ponto em um plano. A seguir,
determine qual o quadrante ao qual pertence o ponto, ou se está sobre um dos eixos cartesianos ou na origem (x = y = 0).

vSe o ponto estiver na origem, escreva a mensagem “Origem”.

Se o ponto estiver sobre um dos eixos escreva “Eixo X” ou “Eixo Y”, conforme for a situação.
"""

valor = input().split()

vlr_x = float(valor[0])
vlr_y = float(valor[1])

if vlr_x == 0 == vlr_y:
    print("Origem")

elif vlr_x > 0:
    if vlr_y > 0:
        print("Q1")

    elif vlr_y < 0:
        print("Q4")

    else:
        print("Eixo X")

elif vlr_x < 0:
    if vlr_y > 0:
        print("Q2")

    elif vlr_y < 0:
        print("Q3")

    else:
        print("Eixo X")

elif vlr_x == 0:
    if vlr_y > 0:
        print("Eixo Y")

    elif vlr_y < 0:
        print("Eixo Y")
