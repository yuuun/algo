n, m = map(int, input().split())
board = []
for i in range(m):
    tmp = list(input())
    if 'R' in tmp:
        r = [i, tmp.index('R')]
    elif 'B' in tmp:
        b = [i, tmp.index('B')]
    board.append(tmp)
