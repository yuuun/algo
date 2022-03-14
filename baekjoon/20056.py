from collections import deque
n, m, k = map(int, input().split())
fireballs = deque()
for _  in range(m):
    r, c, m, s, d = map(int, input().split())
    fireballs.append([r - 1, c - 1, m, s, d])

dxy = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]
maps = [[deque() for _ in range(n)] for _ in range(n)]

def move_fireball():
    while fireballs:
        r, c, m, s, d =  fireballs.popleft()
        r = (r + s * dxy[d][0]) % n
        c = (c + s * dxy[d][1]) % n
        maps[r][c].append([m, s, d])

def split_fireball():
    for i, row_map in enumerate(maps):
        for j, ma in enumerate(row_map):
            length = len(ma)
            if length == 1:
                fireballs.append([i, j] + maps[i][j].popleft())

            elif length > 1:
                tm, ts, cnt_odd, cnt_even = 0, 0, 0, 0
                while maps[i][j]:
                    m, s, d = maps[i][j].popleft()
                    tm += m
                    ts += s

                    if d % 2:
                        cnt_odd += 1
                    else:
                        cnt_even += 1
                if cnt_odd == length or cnt_even == length:
                    dire = [0, 2, 4, 6]
                else:
                    dire = [1, 3, 5, 7]

                m = tm // 5
                if m == 0:
                    continue

                s = ts // length
                for d in dire:
                    fireballs.append([i, j, m, s, d])


for _ in range(k):
    move_fireball()
    split_fireball()

print(sum([fire[2] for fire in fireballs]))