"""
Faça um programa que leia o nome de um vendedor, o seu salário fixo e o total de vendas efetuadas por ele no mês
(em dinheiro). Sabendo que este vendedor ganha 15% de comissão sobre suas vendas efetuadas, informar o total a receber
no final do mês, com duas casas decimais.
"""

NOME_VENDEDOR = input()
SALARIO_VENDEDOR = float(input())
TOTAL_VENDAS = float(input())

SALARIO_FINAL = SALARIO_VENDEDOR + (TOTAL_VENDAS * 0.15)

print("TOTAL = R$ %.2f" % SALARIO_FINAL)
