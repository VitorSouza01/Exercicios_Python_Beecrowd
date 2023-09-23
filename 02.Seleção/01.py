"""
Leia 4 valores inteiros A, B, C e D. A seguir, se B for maior do que C e se D for maior do que A, e a soma de C com D
for maior que a soma de A e B e se C e D, ambos, forem positivos e se a variável A for par escrever a mensagem
"Valores aceitos", senão escrever "Valores nao aceitos".
"""

valores = input().split()

a = int(valores[0])
b = int(valores[1])
c = int(valores[2])
d = int(valores[3])

if b > c:

    if d > a:
        soma_1 = c + d
        soma_2 = a + b

        if soma_1 > soma_2:

            if c and d > 0:

                if a % 2 == 0:
                    print("Valores aceitos")

                else:
                    print("Valores nao aceitos")

            else:
                print("Valores nao aceitos")

        else:
            print("Valores nao aceitos")

    else:
        print("Valores nao aceitos")

else:
    print("Valores nao aceitos")
