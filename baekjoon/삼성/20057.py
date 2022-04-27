n = int(input())
maps = [list(map(int, input().split())) for _ in range(n)]

#방향별 모래
left = [(1, 1, 0.01), (-1, 1, 0.01), (1, 0, 0.07), (-1, 0, 0.07), (1, -1, 0.1),
         (-1, -1, 0.1), (2, 0, 0.02), (-2, 0, 0.02), (0, -2, 0.05), (0, -1, 0)]
right = [(x, -y, z) for x, y, z in left]
down = [(-y, x, z) for x, y, z in left]
up = [(y, x, z) for x, y, z in left]
sx, sy = n // 2, n // 2
cnt = 0

def blow_sand(t, dx, dy, dire):
    global cnt, sx, sy
    for _ in range(t):
        sx += dx
        sy += dy
        if sy < 0:
            break

        sub_a = 0
        for dx, dy, z in dire:
            nx = sx + dx
            ny = sy + dy
            if z == 0: # a
                new_sand = maps[sx][sy] - sub_a
            else:
                new_sand = int(maps[sx][sy] * z)
                sub_a += new_sand
            
            if 0 <= nx < n and 0 <= ny < n:
                maps[nx][ny] += new_sand
            else:
                cnt += new_sand

for i in range(1, n + 1):
    if i % 2:
        blow_sand(i, 0, -1, left)
        blow_sand(i, 1, 0, down)
    else:
        blow_sand(i, 0, 1, right)
        blow_sand(i, -1, 0, up)
print(cnt)