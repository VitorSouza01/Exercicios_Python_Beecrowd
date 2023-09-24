"""
Leia um valor inteiro N. Este valor será a quantidade de valores inteiros X que serão lidos em seguida.
Mostre quantos destes valores X estão dentro do intervalo [10,20] e quantos estão fora do intervalo, mostrando essas
informações.
"""

n = int(input())
loop_in = 0
loop_out = 0

if n < 10000:

    for m in range(n):
        valor = int(input())

        if 10 <= valor <= 20:
            loop_in += 1

        else:
            loop_out += 1

print("%i in" % loop_in)
print("%i out" % loop_out)
