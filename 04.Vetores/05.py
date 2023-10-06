"""
Faça um programa que leia um valor e apresente o número de Fibonacci correspondente a este valor lido. Lembre que os 2
primeiros elementos da série de Fibonacci são 0 e 1 e cada próximo termo é a soma dos 2 anteriores a ele. Todos os
valores de Fibonacci calculados neste problema devem caber em um inteiro de 64 bits sem sinal.
"""

t = int(input())

for i in range(t):

    n = int(input())

    if n <= 0:
        fibonacci_atual = 0

    elif n == 1:
        fibonacci_atual = 1

    else:
        fibonacci_prev = 0
        fibonacci_atual = 1

        for m in range(2, n + 1):

            fibonacci_temp = fibonacci_atual
            fibonacci_atual = (fibonacci_atual + fibonacci_prev) % (2 ** 64)
            fibonacci_prev = fibonacci_temp

    print("Fib(%i) =" % n, fibonacci_atual)
