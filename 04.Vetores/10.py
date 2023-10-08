"""
Um treinador de voleibol gostaria de manter estatísticas sobre sua equipe. A cada jogo, seu auxiliar anota quantas
tentativas de saques, bloqueios e ataques cada um de seus jogadores fez, bem como quantos desses saques, bloqueios e
ataques tiveram sucesso (resultaram em pontos). Seu programa deve mostrar qual o percentual de saques, bloqueios e
ataques do time todo tiveram sucesso.
"""

n = int(input())
s, b, a, s1, b1, a1 = [], [], [], [], [], []
perc_s, perc_b, perc_a = 0, 0, 0

if 1 <= n <= 100:

    for o in range(n):
        nome_do_jogador = input()

        tentativas = input().split()
        s.append(int(tentativas[0]))
        b.append(int(tentativas[1]))
        a.append(int(tentativas[2]))

        sucessos = input().split()
        s1.append(int(sucessos[0]))
        b1.append(int(sucessos[1]))
        a1.append(int(sucessos[2]))

for p in range(n):
    if 0 <= s1[p] <= s[p]:
        perc_s = ((sum(s1) * 100) / sum(s))

    if 0 <= b1[p] <= b[p]:
        perc_b = ((sum(b1) * 100) / sum(b))

    if 0 <= a1[p] <= a[p]:
        perc_a = ((sum(a1) * 100) / sum(a))

print("Pontos de Saque: %.2f" % perc_s, "%.")
print("Pontos de Bloqueio: %.2f" % perc_b, "%.")
print("Pontos de Ataque: %.2f" % perc_a, "%.")
