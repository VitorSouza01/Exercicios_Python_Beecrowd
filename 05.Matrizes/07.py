def main():
    while True:
        try:
            N, M = map(int, input().split())
            tabuleiro = [list(map(int, input().split())) for _ in range(N)]

            for i in range(N):
                for j in range(M):
                    if tabuleiro[i][j] == 1:
                        print('9', end='')
                    else:
                        cont = 0
                        for x in range(max(0, i - 1), min(N, i + 2)):
                            for y in range(max(0, j - 1), min(M, j + 2)):
                                if tabuleiro[x][y] == 1:
                                    cont += 1
                        print(cont, end='')
                print()

        except EOFError:
            break


if __name__ == "__main":
    main()
