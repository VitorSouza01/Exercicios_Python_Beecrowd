"""
Leia a hora inicial e a hora final de um jogo. A seguir calcule a duração do jogo, sabendo que o mesmo pode começar em
um dia e terminar em outro, tendo uma duração mínima de 1 hora e máxima de 24 horas.
"""

horas = input().split()

for x in range(2):
    horas[x] = int(horas[x])

hora_a = int(horas[0])
hora_b = int(horas[1])

if hora_a == hora_b:
    print("O JOGO DUROU 24 HORA(S)")

elif hora_a > hora_b:
    print("O JOGO DUROU %.i HORA(S)" % (-(hora_a - hora_b) + 24))

elif hora_a < hora_b:
    print("O JOGO DUROU %.i HORA(S)" % (-(hora_a - hora_b)))
