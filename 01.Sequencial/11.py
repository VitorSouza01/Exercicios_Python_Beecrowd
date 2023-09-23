"""
Neste problema, deve-se ler o código de uma peça 1, o número de peças 1, o valor unitário de cada peça 1, o código de
uma peça 2, o número de peças 2 e o valor unitário de cada peça 2. Após, calcule e mostre o valor a ser pago.
"""

PROD_1 = (input()).split()
PROD_2 = (input()).split()

PRE_PROD_1 = int(PROD_1[1]) * float(PROD_1[2])
PRE_PROD_2 = int(PROD_2[1]) * float(PROD_2[2])
PRE_PROD_FIN = PRE_PROD_1 + PRE_PROD_2

print("VALOR A PAGAR: R$ %.2f" % PRE_PROD_FIN)
