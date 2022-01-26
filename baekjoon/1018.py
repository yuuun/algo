n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]

mini = []
for i in range(n - 7):
    for j in range(m - 7):
        idx = 0
        for k in range(i, i + 8):
            for l in range(j, j + 8):
                if (k + l) % 2 == 0:
                    if board[k][l] != 'W':
                        idx += 1
                else:
                    if board[k][l] != 'B':
                        idx += 1
        mini += [idx, 64 - idx]
print(min(mini))