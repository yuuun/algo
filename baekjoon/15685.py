n = int(input())
maps = [[0] * 101 for _ in range(101)]
# 0: 오른쪽, 1: 위쪽, 2: 왼쪽, 3: 아래쪽
dxy = [[0, 1], [-1, 0], [0, -1], [1, 0]]
for _ in range(n):
    y, x, d, g = map(int, input().split())
    maps[x][y] = 1

    curve = [d]
    for _ in range(g):
        for c in curve[::-1]:
            curve.append((c + 1) % 4)
    
    for c in curve:
        x += dxy[c][0]
        y += dxy[c][1]
        maps[x][y] = 1


cnt = 0
for i in range(100):
    for j in range(100):
        if maps[i][j] == 1 and maps[i + 1][j] == 1 and maps[i][j + 1] == 1 and maps[i + 1][j + 1] == 1:
            cnt += 1
print(cnt)