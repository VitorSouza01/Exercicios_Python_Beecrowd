"""
Neste problema você deverá ler 15 valores colocá-los em 2 vetores conforme estes valores forem pares ou ímpares. Só
que o tamanho de cada um dos dois vetores é de 5 posições. Então, cada vez que um dos dois vetores encher, você deverá
imprimir todo o vetor e utilizá-lo novamente para os próximos números que forem lidos. Terminada a leitura, deve-se
imprimir o conteúdo que restou em cada um dos dois vetores, imprimindo primeiro os valores do vetor impar. Cada vetor
pode ser preenchido tantas vezes quantas for necessário.
"""

lista_par = []
lista_impar = []
lista_nova = []

for n in range(15):
    valor = int(input())

    if valor % 2 == 0:
        lista_par.append(valor)

    elif valor % 2 != 0:
        lista_impar.append(valor)


lista_nova.append(lista_par)
lista_nova.append(lista_impar)

lista_par_cort = []
lista_impar_cort = []


if len(lista_nova[1]) > 5:
    lista_impar_cort = lista_nova[1][5:].copy()
    del(lista_nova[1][5:])
    lista_nova.append(lista_impar_cort)

if len(lista_nova[0]) > 5:
    lista_par_cort = lista_nova[0][5:].copy()
    del(lista_nova[0][5:])
    lista_nova.append(lista_par_cort)


for o in range(len(lista_nova)):

    if lista_nova[o][0] % 2 == 0:

        for p in range(len(lista_nova[o])):
            print("par[%i] =" % p, lista_nova[o][p])

    elif lista_nova[o][0] % 2 != 0:

        for q in range(len(lista_nova[o])):
            print("impar[%i] =" % q, lista_nova[o][q])
