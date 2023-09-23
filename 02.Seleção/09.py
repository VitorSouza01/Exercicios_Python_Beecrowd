"""
Leia 2 valores inteiros (A e B). Após, o programa deve mostrar uma mensagem "Sao Multiplos" ou "Nao sao Multiplos",
indicando se os valores lidos são múltiplos entre si.
"""

valores = input().split()

vlr_a = int(valores[0])
vlr_b = int(valores[1])

if vlr_b % vlr_a == 0 or vlr_a % vlr_b == 0:
    print("Sao Multiplos")

else:
    print("Nao sao Multiplos")
