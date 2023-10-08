"""
Neste problema você deverá ler 15 valores colocá-los em 2 vetores conforme estes valores forem pares ou ímpares. Só
que o tamanho de cada um dos dois vetores é de 5 posições. Então, cada vez que um dos dois vetores encher, você deverá
imprimir todo o vetor e utilizá-lo novamente para os próximos números que forem lidos. Terminada a leitura, deve-se
imprimir o conteúdo que restou em cada um dos dois vetores, imprimindo primeiro os valores do vetor impar. Cada vetor
pode ser preenchido tantas vezes quantas for necessário.
"""

vetor_par = []
vetor_impar = []

for n in range(15):
    valor = int(input())

    if valor % 2 == 0:
        vetor_par.append(valor)

    else:
        vetor_impar.append(valor)

    if len(vetor_par) == 5:
        for o in range(5):
            print("par[%i] =" % o, vetor_par[o])
        vetor_par = []

    if len(vetor_impar) == 5:
        for p in range(5):
            print("impar[%i] =" % p, vetor_impar[p])
        vetor_impar = []


if len(vetor_impar) < 5:
    for r in range(len(vetor_impar)):
        print("impar[%i] =" % r, vetor_impar[r])

if len(vetor_par) < 5:
    for q in range(len(vetor_par)):
        print("par[%i] =" % q, vetor_par[q])
