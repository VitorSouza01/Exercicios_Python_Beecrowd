"""
Escreva um programa que leia o número de um funcionário, seu número de horas trabalhadas, o valor que recebe por hora e
calcula o salário desse funcionário. A seguir, mostre o número e o salário do funcionário, com duas casas decimais.
"""

NMR_FUNC = int(input())
HR_FUNC = int(input())
VLR_HR = float(input())

SLR_HR = HR_FUNC * VLR_HR

print("NUMBER = %i" % NMR_FUNC)
print("SALARY = U$ %.2f" % SLR_HR)
