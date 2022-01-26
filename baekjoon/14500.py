n, m = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]
dxys = [[[0, 0], [1, 0], [0, 1], [1, 1]],
        [[0, 0], [1, 0], [2, 0], [3, 0]],
        [[0, 0], [0, 1], [0, 2], [1, 1]], [[1, 0], [1, 1], [1, 2], [0, 1]],
        [[0, 0], [1, 0], [1, 1], [2, 1]], [[1, 0], [1, 1], [2, 0], [0, 1]],
        [[0, 0], [1, 0], [2, 0], [2, 1]], [[0, 0], [1, 0], [0, 1], [0, 2]], [[0, 0], [0, 1], [1, 1], [2, 1]], [[1, 0], [1, 1], [1, 2], [0, 2]]]
max_val = 0

for x in range(n):
    for y in range(m):
        for dxy in dxys:
            sum_val = 0
            isFig = True
            for dx, dy in dxy:
                nx, ny = x + dx, y + dy
                if nx < n and ny < m:
                    sum_val += maps[nx][ny]
                else:
                    isFig = False
                    break
            if isFig:
                max_val = max(max_val, sum_val)
            
            if dxy != dxys[0]:
                sum_val = 0
                isFig = True
                for dy, dx in dxy:
                    nx, ny = x + dx, y + dy
                    if nx < n and ny < m:
                        sum_val += maps[nx][ny]
                    else:
                        isFig = False
                        break
                if isFig:
                    max_val = max(max_val, sum_val)

print(max_val)