from collections import deque

dxy = [[0, 1], [1, 0], [0, -1], [-1, 0]]
def sol(x, y, val):
    global n, m, maps, total_cnt, min_val
    check = deque()
    for dx, dy in dxy:
        nx, ny = x + dx, y + dy
        while 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == '.':
            maps[nx][ny] = '#'
            total_cnt -= 1
            check.append([nx, ny])
            nx += dx
            ny += dy

        if check:
            sol(nx - dx, ny - dy, val + 1)
        
        while check:
            nx, ny = check.popleft()
            maps[nx][ny] = '.'
            total_cnt += 1

    if not total_cnt:
        min_val = min(min_val, val)

s = 1
while True:
    try:
        n, m = map(int, input().split())
        maps = []
        total_cnt = n * m
        for i in range(n):
            tmp = list(input())
            for j in range(m):
                if tmp[j] == '*':
                    total_cnt -= 1
            maps.append(tmp)
        
        min_val = 1e10

        for i in range(n):
            for j in range(m):
                if maps[i][j] == '.':
                    maps[i][j] = '#'
                    total_cnt -= 1
                    sol(i, j, 0)
                    maps[i][j] = '.'
                    total_cnt += 1
        if min_val == 1e10:
            min_val = -1
        print('Case {0}: {1}'.format(s, min_val))
        s += 1
        
    except EOFError:
        break