from collections import deque
r, c = map(int, input().split())
water = deque()
maps = []
for i in range(r):
    tmp = list(input())
    for j in range(c):
        if tmp[j].isnumeric():
            tmp[j] = int(tmp[j])
        else:
            tmp[j] = 0
            water.append([i, j])
    maps.append(tmp)

dxy = [[0, 1], [0, -1], [1, 0], [-1, 0], [1, 1], [1, -1], [-1, 1], [-1, -1]]
cnt_list = [[0] * c for _ in range(r)]
ans = 0
while water:
    x, y = water.popleft()
    for dx, dy in dxy:
        nx, ny = x + dx, y + dy
        if 0 <= nx < r and 0 <= ny < c:
            if maps[nx][ny]:
                maps[nx][ny] -= 1
                if maps[nx][ny] == 0:
                    water.append([nx, ny])
                    cnt_list[nx][ny] =  cnt_list[x][y] + 1
                    ans = max(ans, cnt_list[nx][ny])
print(ans)