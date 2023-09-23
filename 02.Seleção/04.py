"""
Com base na tabela abaixo, escreva um programa que leia o código de um item e a quantidade deste item. A seguir,
calcule e mostre o valor da conta a pagar.
"""

valor = input().split()

if int(valor[0]) == 1:
    produto = 4.00 * float(valor[1])
    print("Total: R$ %.2f" % produto)

elif int(valor[0]) == 2:
    produto = 4.50 * float(valor[1])
    print("Total: R$ %.2f" % produto)

elif int(valor[0]) == 3:
    produto = 5.00 * float(valor[1])
    print("Total: R$ %.2f" % produto)

elif int(valor[0]) == 4:
    produto = 2.00 * float(valor[1])
    print("Total: R$ %.2f" % produto)

elif int(valor[0]) == 5:
    produto = 1.50 * float(valor[1])
    print("Total: R$ %.2f" % produto)
