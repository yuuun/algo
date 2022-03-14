n, m, k = map(int, input().split())
maps = [[[] for _ in range(n)] for _ in range(n)]
for _  in range(m):
    r, c, m, s, d = map(int, input().split())
    maps[r - 1][c - 1].append([m, s, d])

dxy = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]
def move_fireball():
    new_map = [[[] for _ in range(n)] for _ in range(n)]
    for i, row_map in enumerate(maps):
        for j, ma in enumerate(row_map):
            for m, s, d in ma:
                r = (dxy[d][0] * s + i) % n
                c = (dxy[d][1] * s + j) % n
                new_map[r][c].append([m, s, d])

    return new_map

def split_fireball():
    new_map = [[[] for _ in range(n)] for _ in range(n)]
    for i, row_map in enumerate(maps):
        for j, ma in enumerate(row_map):
            length = len(ma)
            if length == 1:
                new_map[i][j].append(ma[0])
            elif length > 1:
                tm, ts, cnt_odd, cnt_even = 0, 0, 0, 0
                for m, s, d in ma:
                    tm += m
                    ts += s
                    if d % 2 == 1:
                        cnt_odd += 1
                    else:
                        cnt_even += 1

                m = tm // 5
                if m == 0:
                    continue

                s = ts // length
                if cnt_odd == length or cnt_even == length:
                    dire = [0, 2, 4, 6]
                else:
                    dire = [1, 3, 5, 7]
                
                for d in dire:
                    new_map[i][j].append([m, s, d])
    return new_map


for _ in range(k):
    maps = move_fireball()
    maps = split_fireball()
ans = 0
for i, row_map in enumerate(maps):
    for j, ma in enumerate(row_map):
        for m, _, _ in ma:
            ans += m

print(ans)