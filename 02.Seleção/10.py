"""
Leia 3 valores de ponto flutuante A, B e C e ordene-os em ordem decrescente, de modo que o lado A representa o maior
dos 3 lados. A seguir, determine o tipo de triângulo que estes três lados formam, com base nos seguintes casos, sempre
escrevendo uma mensagem adequada:

se A ≥ B+C, apresente a mensagem: NAO FORMA TRIANGULO
se A2 = B2 + C2, apresente a mensagem: TRIANGULO RETANGULO
se A2 > B2 + C2, apresente a mensagem: TRIANGULO OBTUSANGULO
se A2 < B2 + C2, apresente a mensagem: TRIANGULO ACUTANGULO
se os três lados forem iguais, apresente a mensagem: TRIANGULO EQUILATERO
se apenas dois dos lados forem iguais, apresente a mensagem: TRIANGULO ISOSCELES
"""

valores = input().split()

for x in range(3):
    valores[x] = float(valores[x])

valores.sort(reverse=True)

a = valores[0]
b = valores[1]
c = valores[2]

if a >= (b + c):
    print("NAO FORMA TRIANGULO")

elif (a * a) == (b * b) + (c * c):
    print("TRIANGULO RETANGULO")

elif (a * a) > (b * b) + (c * c):
    print("TRIANGULO OBTUSANGULO")

elif (a * a) < (b * b) + (c * c):
    print("TRIANGULO ACUTANGULO")

if a == b == c:
    print("TRIANGULO EQUILATERO")

elif a == b or a == c or b == c:
    print("TRIANGULO ISOSCELES")
